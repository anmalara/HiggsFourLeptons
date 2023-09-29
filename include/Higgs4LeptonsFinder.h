#pragma once

#include "LEAF/Analyzer/include/Config.h"
#include "LEAF/Analyzer/include/AnalysisModule.h"
#include "LEAF/HiggsFourLeptons/include/HiggsFourLeptonsEvent.h"

class Higgs4LeptonsFinder: public AnalysisModule<HiggsFourLeptonsEvent> {
public:
  explicit Higgs4LeptonsFinder(const Config& cfg);
  virtual ~Higgs4LeptonsFinder() = default;
  virtual bool process(HiggsFourLeptonsEvent & event) override;

  bool Fail_GhostLeptons(const FlavorParticle& lep1,const FlavorParticle& lep2,const FlavorParticle& lep3,const FlavorParticle& lep4);
  bool Fail_LeptonPts(const FlavorParticle& lep1,const FlavorParticle& lep2,const FlavorParticle& lep3,const FlavorParticle& lep4);
  bool Fail_LeptonInvMass(const FlavorParticle& lep1,const FlavorParticle& lep2,const FlavorParticle& lep3,const FlavorParticle& lep4);
  bool Fail_QCDSuppression(const FlavorParticle& lep1,const FlavorParticle& lep2,const FlavorParticle& lep3,const FlavorParticle& lep4);
  bool Fail_ZMassMax(const TLorentzVector& Z1);
  bool Fail_Z1MassMin(const TLorentzVector& Z1);
  bool Fail_Z2MassMin(const TLorentzVector& Z2);
  bool Fail_SmartCut(const FlavorParticle& lep1,const FlavorParticle& lep2,const FlavorParticle& lep3,const FlavorParticle& lep4);
  bool Fail_CrossCleaning(const Electron& el1, const vector<Muon>& muons,const vector<bool>& lep_bool, const vector<int>& lep_indices);
};
