#include "LEAF/Analyzer/include/constants.h"
#include "LEAF/HiggsFourLeptons/include/HiggsFourLeptonsEvent.h"


using namespace std;

void HiggsFourLeptonsEvent::SetNewVectors(){
  H_muons = new vector<Muon>;
  H_electrons = new vector<Electron>;
  H_leptons = new vector<FlavorParticle>;
  reco_Z_bosons = new vector<TLorentzVector>;
  reco_H_bosons = new vector<TLorentzVector>;
  H_chi2 = new std::vector<float>;
  Z1_chi2 = new std::vector<float>;
  Z2_chi2 = new std::vector<float>;
  HZZ_chi2 = new std::vector<float>;
}


void HiggsFourLeptonsEvent::SetNewScalars(){
  m_eventCategory = "undefined";
}

void HiggsFourLeptonsEvent::DeleteVectors(){
  delete H_muons;
  delete H_electrons;
  delete H_leptons;
  delete reco_Z_bosons;
  delete reco_H_bosons;
  delete H_chi2;
  delete Z1_chi2;
  delete Z2_chi2;
  delete HZZ_chi2;
}

void HiggsFourLeptonsEvent::ResetVectors(){
  H_muons = 0;
  H_electrons = 0;
  H_leptons = 0;
  reco_Z_bosons = 0;
  reco_H_bosons = 0;
  H_chi2 = 0;
  Z1_chi2 = 0;
  Z2_chi2 = 0;
  HZZ_chi2 = 0;
}


HiggsFourLeptonsEvent::HiggsFourLeptonsEvent(){
  SetNewVectors();
  SetNewScalars();
}

HiggsFourLeptonsEvent::~HiggsFourLeptonsEvent(){
  DeleteVectors();
}

void HiggsFourLeptonsEvent::clear(){
  RecoEvent::clear();
  DeleteVectors();
  ResetVectors();
  SetNewScalars();
}

void HiggsFourLeptonsEvent::reset(){
  RecoEvent::reset();
  DeleteVectors();
  SetNewVectors();
  SetNewScalars();
}
