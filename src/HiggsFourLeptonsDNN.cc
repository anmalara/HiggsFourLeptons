#include "LEAF/HiggsFourLeptons/include/HiggsFourLeptonsDNN.h"
#include "LEAF/HiggsFourLeptons/include/Utils.h"

#include <bits/stdc++.h>
#include <cmath>
using namespace std;
using namespace cms::Ort;

HiggsFourLeptonsDNN::HiggsFourLeptonsDNN(const Config& cfg) {

  ONNX_inference.reset(new ONNXRuntime("/user/bhonore/WorkingArea/CMSSW_10_6_28/src/LEAF/HiggsFourLeptons/data/dnn_models/model_ops12.onnx"));

};

bool HiggsFourLeptonsDNN::process(HiggsFourLeptonsEvent& event) {

  bool printing = true;

  std::vector<PFCandidate> candidates(0);

  for(const PFCandidate& cand: *event.pfcands){
    if (cand.fromPV()!=3) continue;
    if(cand.pt()<0.2) continue;
    if(cand.eta()>5.2) continue;
    int cand_id = fabs(cand.type());
    if (cand.charge()==0) {
        float cand_pt = cand.pt();
        if (cand_id == 22 && cand_pt<1) continue;
        if ((cand_id==0 || cand_id==1 ||cand_id==2 ||cand_id==130) && cand_pt<3) continue;
        if (cand_id==11 || cand_id==13 || cand_id==211) throw std::runtime_error("Neutral PF identified as e/mu/ch: "+to_string(cand_id));
    } 
    bool keep = true;
    if (cand_id==11 || cand_id==13 || cand_id==22){
    for(const FlavorParticle& selec_lep : *event.H_leptons){
          if(deltaR(cand,selec_lep)<0.4){
            keep = false;
          }        
        } 
    }
    if(keep){
      candidates.push_back(cand);
    }
  }

  sort_by_pt<PFCandidate>(candidates);

  size_t no_candidates = candidates.size();
  unsigned int no_selected_candidates = 100;

  for(size_t i=0;i<no_selected_candidates;++i){
    if(i<no_candidates){
  
      event.eta->push_back(candidates.at(i).eta());
      event.phi->push_back(candidates.at(i).phi());
      event.pt->push_back(candidates.at(i).pt());
      event.energy->push_back(candidates.at(i).e());
      event.pdgid->push_back(candidates.at(i).pdgid());
      event.charge->push_back(candidates.at(i).charge());
      event.puppiweight->push_back(candidates.at(i).puppiweight());
      event.energy_log->push_back(log(candidates.at(i).e()));
      event.pt_log->push_back(log(candidates.at(i).pt()));
      event.mask->push_back(1.0);
    }else{
      event.eta->push_back(0.0);
      event.phi->push_back(0.0);
      event.pt->push_back(0.0);
      event.energy->push_back(0.0);
      event.pdgid->push_back(0.0);
      event.charge->push_back(0.0);
      event.puppiweight->push_back(0.0);
      event.energy_log->push_back(0.0);
      event.pt_log->push_back(0.0);
      event.mask->push_back(0.0);

    }
  }

  const vector<string>& input_names = {"pf_points", "pf_features", "pf_mask"};
  const vector<vector<int64_t>>& input_shapes = {{1,2,no_selected_candidates},{1,9,no_selected_candidates},{1,1,no_selected_candidates}};
  vector<vector<float>> input_data;

  std::vector<float> points, features, mask;

  points.insert( points.end(), event.eta->begin(), event.eta->end() );
  points.insert( points.end(), event.phi->begin(), event.phi->end() );

  features.insert( features.end(), event.pt->begin(), event.pt->end() );
  features.insert( features.end(), event.eta->begin(), event.eta->end() );
  features.insert( features.end(), event.phi->begin(), event.phi->end() );
  features.insert( features.end(), event.energy->begin(), event.energy->end() );
  features.insert( features.end(), event.pdgid->begin(), event.pdgid->end() );
  features.insert( features.end(), event.charge->begin(), event.charge->end() );
  features.insert( features.end(), event.puppiweight->begin(), event.puppiweight->end() );
  features.insert( features.end(), event.energy_log->begin(), event.energy_log->end() );
  features.insert( features.end(), event.pt_log->begin(), event.pt_log->end() );

  mask.insert( mask.end(), event.mask->begin(), event.mask->end() );


  input_data.push_back(points);
  input_data.push_back(features);
  input_data.push_back(mask);

  vector<vector<float>> outputs = ONNX_inference->run(input_names, input_data, input_shapes);

  event.set_dnn_output(outputs[0][0]);
  if(printing){
    std::cout << "N PF " << event.pfcands->size() << std::endl;
    cout<<"DNN output "<<outputs[0][0]<<endl;
    std::cout << std::endl << "output data -> ";
    for (auto &i: outputs[0]) { std::cout << i << " "; }
    std::cout << std::endl;
    cout << candidates.size() << endl;
  }
  return true;

}

