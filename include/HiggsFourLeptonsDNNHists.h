#pragma once

#include "LEAF/Analyzer/include/BaseHists.h"
#include "LEAF/HiggsFourLeptons/include/HiggsFourLeptonsEvent.h"
#include "LEAF/HiggsFourLeptons/include/HiggsFourLeptonsHists.h"
#include "LEAF/Analyzer/include/GenLevelConstants.h"

using namespace std;

class HiggsFourLeptonsDNNHists : public BaseHists{

public:
  // Constructors, destructor
  HiggsFourLeptonsDNNHists(TString dir_);
  HiggsFourLeptonsDNNHists(const HiggsFourLeptonsDNNHists &) = default;
  HiggsFourLeptonsDNNHists & operator = (const HiggsFourLeptonsDNNHists &) = default;
  ~HiggsFourLeptonsDNNHists() = default;

  // Main functions
  void fill(const HiggsFourLeptonsEvent & event) override;

  vector<ParticleType> get_types() const {return types;}

private:
  int max_index;
  const vector<ParticleType> types = {ParticleType::e, ParticleType::mu, ParticleType::gamma, ParticleType::h, ParticleType::h0, ParticleType::h_HF, ParticleType::egamma_HF, ParticleType::X};

};
