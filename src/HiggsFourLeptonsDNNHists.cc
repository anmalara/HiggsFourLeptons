#include "LEAF/Analyzer/include/constants.h"
#include "LEAF/Analyzer/include/useful_functions.h"

#include "LEAF/HiggsFourLeptons/include/Utils.h"
#include "LEAF/HiggsFourLeptons/include/HiggsFourLeptonsDNNHists.h"
#include "LEAF/HiggsFourLeptons/include/HiggsFourLeptonsHists.h"
#include "LEAF/Analyzer/include/GenLevelUtils.h"

using namespace std;

HiggsFourLeptonsDNNHists::HiggsFourLeptonsDNNHists(TString dir_) : BaseHists(dir_){
    int n_types = get_types().size();
    book<TH1F>("sumweights",        ";sum of event weights; Events / bin",          1,          0.5,        1.5);
    book<TH1F>("pt_cand",           ";p_{T};Events / bin",                          40,         0.0,        20.0);
    book<TH1F>("eta_cand",               ";eta;Events / bin",                       52,        -5.2,        5.2);
    book<TH1F>("phi_cand",               ";phi;Events / bin",                       52,        -5.2,        5.2);
    book<TH1F>("energy_cand",                ";energy;Events / bin",                70,         0.0,        70.0);
    book<TH1F>("pdgid_cand",                 ";pdgid;Events / bin",                 n_types,    0.0,        n_types);
    book<TH1F>("charge_cand",                ";charge;Events / bin",                3,          -1.5,       1.5);
    book<TH1F>("puppiweight_cand",               ";puppiweight;Events / bin",       100,        0.0,        1.1);
    book<TH1F>("mask_cand",              ";mask;Events / bin",                      2,          0.0,        1.1);
    book<TH1F>("DNN_score", ";DNN score;Events / bin",                              50,         0.0,        1.0);

    int index = 1;
    for(auto type : get_types()){
        hist<TH1F>("pdgid_cand")->GetXaxis()->SetBinLabel(index,type2str(type).c_str());
        ++index;
    }

}

void HiggsFourLeptonsDNNHists::fill(const HiggsFourLeptonsEvent & event){
    double weight = event.weight;
    hist<TH1F>("sumweights")->Fill(1, weight);

    size_t no_selected_candidates = event.mask->size();

    for(size_t i=0;i<no_selected_candidates;++i){
        hist<TH1F>("mask_cand")->Fill(event.mask->at(i),weight);
        if(event.mask->at(i)==0.0) continue;
        hist<TH1F>("pt_cand")->Fill(event.pt->at(i),weight);
        hist<TH1F>("eta_cand")->Fill(event.eta->at(i),weight);
        hist<TH1F>("phi_cand")->Fill(event.phi->at(i),weight);
        hist<TH1F>("energy_cand")->Fill(event.energy->at(i),weight);

        string type = type2str((int)fabs(event.pdgid->at(i)));
        hist<TH1F>("pdgid_cand")->Fill(type.c_str(), weight);
        hist<TH1F>("charge_cand")->Fill(event.charge->at(i),weight);
        hist<TH1F>("puppiweight_cand")->Fill(event.puppiweight->at(i),weight);
        hist<TH1F>("DNN_score")->Fill(event.dnn_output(),weight);
    }

}