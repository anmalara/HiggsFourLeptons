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

  pt = new std::vector<float>;
  eta = new std::vector<float>;
  phi = new std::vector<float>;
  energy = new std::vector<float>;
  pdgid = new std::vector<float>;
  charge = new std::vector<float>;
  puppiweight = new std::vector<float>;
  energy_log = new std::vector<float>;
  pt_log = new std::vector<float>;
  mask = new std::vector<float>;
}


void HiggsFourLeptonsEvent::SetNewScalars(){
  m_eventCategory = "undefined";
  m_dnn_output = -1;
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

  delete pt;
  delete eta;
  delete phi;
  delete energy;
  delete pdgid;
  delete charge;
  delete puppiweight;
  delete energy_log;
  delete pt_log;
  delete mask;
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

  pt = 0;
  eta = 0;
  phi = 0;
  energy = 0;
  pdgid = 0;
  charge = 0;
  puppiweight = 0;
  energy_log = 0;
  pt_log = 0;
  mask = 0;
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


