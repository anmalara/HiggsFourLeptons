#pragma once

#include "LEAF/Analyzer/include/BaseHists.h"
#include "LEAF/HiggsFourLeptons/include/HiggsFourLeptonsEvent.h"

using namespace std;

class HiggsFourLeptonsHists : public BaseHists{

public:
  // Constructors, destructor
  HiggsFourLeptonsHists(TString dir_);
  HiggsFourLeptonsHists(const HiggsFourLeptonsHists &) = default;
  HiggsFourLeptonsHists & operator = (const HiggsFourLeptonsHists &) = default;
  ~HiggsFourLeptonsHists() = default;

  // Main functions
  void fill(const HiggsFourLeptonsEvent & event);


private:
  int max_index;
  const vector<ParticleType> labels_pdgids = {ParticleType::e,
                                      ParticleType::mu,
                                      ParticleType::gamma,
                                      ParticleType::h,
                                      ParticleType::h0,
                                      ParticleType::h_HF,
                                      ParticleType::egamma_HF,
                                      ParticleType::X};
  vector<TString> eleIso_variables_labels = {"iso_rel_03",
                                             "iso_rel_03_charged"};

  vector<TString> muoIso_variables_labels = {"iso_rel_04",
                                             "iso_rel_03",
                                             "iso_rel_03_charged",
                                             "iso_tk"};



};
