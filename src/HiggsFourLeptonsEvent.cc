#include "LEAF/Analyzer/include/constants.h"
#include "LEAF/HiggsFourLeptons/include/HiggsFourLeptonsEvent.h"


using namespace std;

void HiggsFourLeptonsEvent::SetNewVectors(){
  H_muons = new vector<Muon>;
  H_electrons = new vector<Electron>;
  H_leptons = new vector<FlavorParticle>;
  reco_Z_bosons = new vector<TLorentzVector>;
  reco_H_bosons = new vector<TLorentzVector>;
}


void HiggsFourLeptonsEvent::SetNewScalars(){
  m_H_chi2 = -1;
  m_Z1_chi2 = -1;
  m_Z2_chi2 = -1;
  m_HZZ_chi2 = -1;
  m_eventCategory = -1;
}

void HiggsFourLeptonsEvent::DeleteVectors(){
  delete H_muons;
  delete H_electrons;
  delete H_leptons;
  delete reco_Z_bosons;
  delete reco_H_bosons;
}

void HiggsFourLeptonsEvent::ResetVectors(){
  H_muons = 0;
  H_electrons = 0;
  H_leptons = 0;
  reco_Z_bosons = 0;
  reco_H_bosons = 0;
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
