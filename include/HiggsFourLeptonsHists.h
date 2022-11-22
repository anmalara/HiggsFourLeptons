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

};
