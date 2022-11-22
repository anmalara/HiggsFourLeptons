#include "LEAF/HiggsFourLeptons/include/Higgs4LeptonsFinder.h"
#include "LEAF/HiggsFourLeptons/include/Utils.h"

using namespace std;

Higgs4LeptonsFinder::Higgs4LeptonsFinder(const Config& cfg) {};

bool Higgs4LeptonsFinder::process(HiggsFourLeptonsEvent& event) {
  vector<int>  lep_indices;
  vector<bool> lep_bool;

  for(size_t i=0; i<(*event.electrons).size(); i++){
    const Electron lep1 = (*event.electrons).at(i);
    for(size_t j=i+1; j<(*event.electrons).size(); j++){
      const Electron lep2 = (*event.electrons).at(j);
      if (lep1.charge()==lep2.charge()) continue;
      // TLorentzVector z1 = lep1.p4()+lep2.p4();
      // if (fabs(z1.M()-Z_mass_reco)>Z_width_reco && fabs(z1.M()-Z_mass_offshell_reco)>Z_width_offshell_reco ) continue;
      if ( std::find(lep_indices.begin(), lep_indices.end(), i) == lep_indices.end() ) {
        lep_indices.push_back(i);
        lep_bool.push_back(true);
      }
      if ( std::find(lep_indices.begin(), lep_indices.end(), j) == lep_indices.end() ) {
        lep_indices.push_back(j);
        lep_bool.push_back(true);
      }
      // cout << "checking electrons: " << lep1.charge() << " " << lep2.charge() << " "<< i << " " << j << " " << lep1.charge() << " " << lep2.charge() << " " << z1.M() <<endl;
    }
  }

  for(size_t i=0; i<(*event.muons).size(); i++){
    Muon lep1 = (*event.muons).at(i);
    for(size_t j=i+1; j<(*event.muons).size(); j++){
      const Muon lep2 = (*event.muons).at(j);
      if (lep1.charge()==lep2.charge()) continue;
      // TLorentzVector z1 = lep1.p4()+lep2.p4();
      // if (fabs(z1.M()-Z_mass_reco)>Z_width_reco && fabs(z1.M()-Z_mass_offshell_reco)>Z_width_offshell_reco ) continue;
      if ( std::find(lep_indices.begin(), lep_indices.end(), i) == lep_indices.end() || (std::find(lep_indices.begin(), lep_indices.end(), i) != lep_indices.end() && lep_bool.at(std::find(lep_indices.begin(), lep_indices.end(), i) - lep_indices.begin())) ) {
        lep_indices.push_back(i);
        lep_bool.push_back(false);
      }
      if ( std::find(lep_indices.begin(), lep_indices.end(), j) == lep_indices.end() || (std::find(lep_indices.begin(), lep_indices.end(), j) != lep_indices.end() && lep_bool.at(std::find(lep_indices.begin(), lep_indices.end(), j) - lep_indices.begin())) ) {
        lep_indices.push_back(j);
        lep_bool.push_back(false);
      }
    }
  }

  if (lep_indices.size()<4) return false;

  float min_chi2 = 1000;
  for(size_t i_1=0; i_1<lep_indices.size(); i_1++){
    int index_1 = lep_indices.at(i_1);
    FlavorParticle lep_1;
    bool is_ele_1 = lep_bool.at(i_1);
    if (is_ele_1) lep_1 = (*event.electrons).at(index_1);
    else lep_1 = (*event.muons).at(index_1);
    for(size_t i_2=i_1+1; i_2<lep_indices.size(); i_2++){
      bool is_ele_2 = lep_bool.at(i_2);
      if (is_ele_1!=is_ele_2) continue;
      int index_2 = lep_indices.at(i_2);
      FlavorParticle lep_2;
      if (is_ele_2) lep_2 = (*event.electrons).at(index_2);
      else lep_2 = (*event.muons).at(index_2);
      if (lep_1.charge()==lep_2.charge()) continue;
      for(size_t i_3=0; i_3<lep_indices.size(); i_3++){
        if (i_1==i_3 || i_2==i_3) continue;
        int index_3 = lep_indices.at(i_3);
        FlavorParticle lep_3;
        bool is_ele_3 = lep_bool.at(i_3);
        if (is_ele_3) lep_3 = (*event.electrons).at(index_3);
        else lep_3 = (*event.muons).at(index_3);
        for(size_t i_4=i_3+1; i_4<lep_indices.size(); i_4++){
          if (i_1==i_4 || i_2==i_4) continue;
          bool is_ele_4 = lep_bool.at(i_4);
          if (is_ele_3!=is_ele_4) continue;
          int index_4 = lep_indices.at(i_4);
          FlavorParticle lep_4;
          if (is_ele_4) lep_4 = (*event.electrons).at(index_4);
          else lep_4 = (*event.muons).at(index_4);
          if (lep_3.charge()==lep_4.charge()) continue;
          TLorentzVector h = lep_1.p4()+lep_2.p4()+lep_3.p4()+lep_4.p4();
          TLorentzVector z1 = lep_1.p4()+lep_2.p4();
          TLorentzVector z2 = lep_3.p4()+lep_4.p4();
          float chi2_z1 = fabs(z1.M()-Z_mass_reco)/Z_width_reco;
          float chi2_z2 = fabs(z2.M()-Z_mass_offshell_reco)/Z_width_offshell_reco;
          float chi2_h  = fabs(h.M()-H_mass_reco)/H_width_reco;
          // if (chi2_z1>1) continue;
          // if (chi2_z2>1) continue;
          if (chi2_h>1) continue;
          float chi2 = chi2_z1+chi2_z2+chi2_h;
          if (chi2< min_chi2) {
            min_chi2 = chi2;
            event.set_Z1_chi2(chi2_z1);
            event.set_Z2_chi2(chi2_z2);
            event.set_H_chi2(chi2_h);
            event.set_HZZ_chi2(chi2);
            event.H_leptons->clear();
            event.H_electrons->clear();
            event.H_muons->clear();
            event.reco_Z_bosons->clear();
            event.reco_H_bosons->clear();
            event.reco_H_bosons->push_back(h);
            event.reco_Z_bosons->push_back(z1);
            event.reco_Z_bosons->push_back(z2);
            event.H_leptons->push_back(lep_1);
            event.H_leptons->push_back(lep_2);
            event.H_leptons->push_back(lep_3);
            event.H_leptons->push_back(lep_4);
            if(is_ele_1) event.H_electrons->push_back((*event.electrons).at(index_1));
            else event.H_muons->push_back((*event.muons).at(index_1));
            if(is_ele_2) event.H_electrons->push_back((*event.electrons).at(index_2));
            else event.H_muons->push_back((*event.muons).at(index_2));
            if(is_ele_3) event.H_electrons->push_back((*event.electrons).at(index_3));
            else event.H_muons->push_back((*event.muons).at(index_3));
            if(is_ele_4) event.H_electrons->push_back((*event.electrons).at(index_4));
            else event.H_muons->push_back((*event.muons).at(index_4));
          }
        }
      }
    }
  }
  sort_by_pt<Electron>(*event.H_electrons);
  sort_by_pt<Muon>(*event.H_muons);
  sort_by_pt<FlavorParticle>(*event.H_leptons);

  if (event.H_leptons->size()!=4) return false;
  return true;

}
