#include "LEAF/HiggsFourLeptons/include/Higgs4LeptonsFinder.h"
#include "LEAF/HiggsFourLeptons/include/Utils.h"

#include <bits/stdc++.h>
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
      TLorentzVector z1 = lep1.p4()+lep2.p4();
      if (Fail_ZMassMax(z1)) continue;
      if (Fail_Z2MassMin(z1)) continue;
      if ( FindInVector<int>(lep_indices, i)<0 ) {
        lep_indices.push_back(i);
        lep_bool.push_back(true);
      }
      if ( FindInVector<int>(lep_indices, j)<0 ) {
        lep_indices.push_back(j);
        lep_bool.push_back(true);
      }
    }
  }

  for(size_t i=0; i<(*event.muons).size(); i++){
    const Muon lep1 = (*event.muons).at(i);
    for(size_t j=i+1; j<(*event.muons).size(); j++){
      const Muon lep2 = (*event.muons).at(j);
      if (lep1.charge()==lep2.charge()) continue;
      TLorentzVector z1 = lep1.p4()+lep2.p4();
      if (Fail_ZMassMax(z1)) continue;
      if (Fail_Z2MassMin(z1)) continue;
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

  vector<vector<int>> used_indices={};
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
        if (i_3==i_1 || i_3==i_2) continue;
        int index_3 = lep_indices.at(i_3);
        FlavorParticle lep_3;
        bool is_ele_3 = lep_bool.at(i_3);
        if (is_ele_3) lep_3 = (*event.electrons).at(index_3);
        else lep_3 = (*event.muons).at(index_3);
        for(size_t i_4=i_3+1; i_4<lep_indices.size(); i_4++){
          if (i_4==i_1 || i_4==i_2) continue;
          vector<int> indices = {int(i_1),int(i_2),int(i_3),int(i_4)};
          sort(indices.begin(), indices.end());
          bool used_set = false;
          for(auto x :used_indices){if (x ==indices) {used_set = true;}}
          if (used_set) continue;
          bool is_ele_4 = lep_bool.at(i_4);
          if (is_ele_3!=is_ele_4) continue;
          int index_4 = lep_indices.at(i_4);
          FlavorParticle lep_4;
          if (is_ele_4) lep_4 = (*event.electrons).at(index_4);
          else lep_4 = (*event.muons).at(index_4);
          if (lep_3.charge()==lep_4.charge()) continue;
          if (Fail_GhostLeptons(lep_1,lep_2,lep_3,lep_4)) continue;
          if (Fail_LeptonPts(lep_1,lep_2,lep_3,lep_4)) continue;
          if (Fail_LeptonInvMass(lep_1,lep_2,lep_3,lep_4)) continue;
          if (Fail_QCDSuppression(lep_1,lep_2,lep_3,lep_4)) continue;
          TLorentzVector z1 = lep_1.p4()+lep_2.p4();
          if (Fail_Z1MassMin(z1)) continue;
          TLorentzVector z2 = lep_3.p4()+lep_4.p4();
          if (Fail_Z2MassMin(z2)) continue;
          if (z1.M()<z2.M()) continue;
          if (Fail_SmartCut(z1,z2)) continue;
          TLorentzVector h = lep_1.p4()+lep_2.p4()+lep_3.p4()+lep_4.p4();
          float chi2_z1 = fabs(z1.M()-Z_mass_reco)/Z_width_reco;
          float chi2_z2 = fabs(z2.M()-Z_mass_offshell_reco)/Z_width_offshell_reco;
          float chi2_h  = fabs(h.M()-H_mass_reco)/H_width_reco;
          float chi2 = chi2_z1+chi2_z2+chi2_h;
          used_indices.push_back(indices);
          event.Z1_chi2->push_back(chi2_z1);
          event.Z2_chi2->push_back(chi2_z2);
          event.H_chi2->push_back(chi2_h);
          event.HZZ_chi2->push_back(chi2);
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

  int n_higgs = (*event.reco_H_bosons).size();
  if (n_higgs==0) return false;
  sort_by_pt<Electron>(*event.H_electrons);
  sort_by_pt<Muon>(*event.H_muons);
  sort_by_pt<FlavorParticle>(*event.H_leptons);

  std::string eventCategory = "undefined";
  if (n_higgs>1) eventCategory = "multiple";
  if (n_higgs==1){
    eventCategory = "";
    if ((*event.reco_H_bosons).at(0).M()>fourLeptonInvMass_min_offshell) eventCategory += "OS-";
    if ((*event.H_muons).size()==4) eventCategory += "4m";
    else if ((*event.H_electrons).size()==4) eventCategory += "4e";
    else eventCategory += "2m2e";
  }
  event.set_eventCategory(eventCategory);
  // if (event.H_leptons->size()!=4) return false;
  return true;

}


bool Higgs4LeptonsFinder::Fail_GhostLeptons(const FlavorParticle& lep1,const FlavorParticle& lep2,const FlavorParticle& lep3,const FlavorParticle& lep4){
  if (deltaR(lep1, lep2)<ghostlepton_dR_min) return true;
  if (deltaR(lep1, lep3)<ghostlepton_dR_min) return true;
  if (deltaR(lep1, lep4)<ghostlepton_dR_min) return true;
  if (deltaR(lep2, lep3)<ghostlepton_dR_min) return true;
  if (deltaR(lep2, lep4)<ghostlepton_dR_min) return true;
  if (deltaR(lep3, lep4)<ghostlepton_dR_min) return true;
  return false;
}

bool Higgs4LeptonsFinder::Fail_LeptonPts(const FlavorParticle& lep1,const FlavorParticle& lep2,const FlavorParticle& lep3,const FlavorParticle& lep4){
  vector<double> lep_pts = { lep1.pt(),lep2.pt(),lep3.pt(),lep4.pt()};
  sort(lep_pts.begin(), lep_pts.end(), greater<double>());
  if (lep_pts.at(0)<lep0_pt_min) return true;
  if (lep_pts.at(1)<lep1_pt_min) return true;
  return false;
}

bool Higgs4LeptonsFinder::Fail_LeptonInvMass(const FlavorParticle& lep1,const FlavorParticle& lep2,const FlavorParticle& lep3,const FlavorParticle& lep4){
  TLorentzVector llll = lep1.p4()+lep2.p4()+lep3.p4()+lep4.p4();
  if (llll.M()<fourLeptonInvMass_min) return true;
  return false;
}

bool Higgs4LeptonsFinder::Fail_ZMassMax(const TLorentzVector& Z1) {
  if (Z1.M()>Z_mass_max) return true;
  return false;
}

bool Higgs4LeptonsFinder::Fail_Z1MassMin(const TLorentzVector& Z1) {
  if (Z1.M()<highest_Z_mass_min) return true;
  return false;
}

bool Higgs4LeptonsFinder::Fail_Z2MassMin(const TLorentzVector& Z2) {
  if (Z2.M()<lower_Z_mass_min) return true;
  return false;
}

bool Higgs4LeptonsFinder::Fail_SmartCut(const TLorentzVector& Z1, const TLorentzVector& Z2) {
  // float m_Za = Z1.M();
  // float m_Zb = Z2.M();
  // if (m_Za<m_Zb) swap(m_Za,m_Zb);
  // if (Z_mass_reco<=m_Zb) swap(m_Za,m_Zb);
  // float d_m_Za = fabs(m_Za-Z_mass_reco);
  // float d_m_Zb = fabs(m_Zb-Z_mass_reco);
  return false;
}

bool Higgs4LeptonsFinder::Fail_QCDSuppression(const FlavorParticle& lep1,const FlavorParticle& lep2,const FlavorParticle& lep3,const FlavorParticle& lep4){
  vector<FlavorParticle> leptons = {lep1,lep2,lep3,lep4};
  // all four opposite-sign pairs (regardless of lepton flavor) to suppress QCD
  for (const FlavorParticle lep1: leptons){
    for (const FlavorParticle lep2: leptons){
      if (lep1.charge()==lep2.charge()) continue;
      TLorentzVector z1 = lep1.p4()+lep2.p4();
      if (z1.M()<Z_mass_min) return true;
    }
  }
  return false;
}
