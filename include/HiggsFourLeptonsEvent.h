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

  float H_chi2() const { return m_H_chi2;}
  float Z1_chi2() const { return m_Z1_chi2;}
  float Z2_chi2() const { return m_Z2_chi2;}
  float HZZ_chi2() const { return m_HZZ_chi2;}
  int eventCategory() const { return m_eventCategory;}

  void set_H_chi2(float x) { m_H_chi2 = x;}
  void set_Z1_chi2(float x) { m_Z1_chi2 = x;}
  void set_Z2_chi2(float x) { m_Z2_chi2 = x;}
  void set_HZZ_chi2(float x) { m_HZZ_chi2 = x;}
  void set_eventCategory(int x) { m_eventCategory = x;}

  vector<Muon>* H_muons;
  vector<Electron>* H_electrons;
  vector<FlavorParticle>* H_leptons;
  vector<TLorentzVector>* reco_Z_bosons;
  vector<TLorentzVector>* reco_H_bosons;

protected:

  float m_H_chi2, m_Z1_chi2, m_Z2_chi2, m_HZZ_chi2;
  int m_eventCategory;
};
