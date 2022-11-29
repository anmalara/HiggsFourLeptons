#pragma once

#include <TString.h>
#include <TH1F.h>
#include <map>
#include <TTreeReader.h>
#include <TTreeReaderValue.h>

#include "LEAF/Analyzer/include/RecoEvent.h"

using namespace std;

// Container class for all quantities
class HiggsFourLeptonsEvent : public RecoEvent{

public:
  // Constructors, destructor
  HiggsFourLeptonsEvent();
  ~HiggsFourLeptonsEvent();

  void clear();
  void reset();

  void SetNewVectors();
  void SetNewScalars();
  void DeleteVectors();
  void ResetVectors();

  std::string eventCategory() const { return m_eventCategory;}
  void set_eventCategory(std::string x) { m_eventCategory = x;}

  vector<Muon>* H_muons;
  vector<Electron>* H_electrons;
  vector<FlavorParticle>* H_leptons;
  vector<TLorentzVector>* reco_Z_bosons;
  vector<TLorentzVector>* reco_H_bosons;
  vector<float>* H_chi2;
  vector<float>* Z1_chi2;
  vector<float>* Z2_chi2;
  vector<float>* HZZ_chi2;

protected:
  std::string m_eventCategory;
};
