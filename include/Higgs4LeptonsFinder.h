#pragma once

#include "LEAF/Analyzer/include/Config.h"
#include "LEAF/Analyzer/include/AnalysisModule.h"
#include "LEAF/HiggsFourLeptons/include/HiggsFourLeptonsEvent.h"

class Higgs4LeptonsFinder: public AnalysisModule<HiggsFourLeptonsEvent> {
public:
  explicit Higgs4LeptonsFinder(const Config& cfg);
  virtual ~Higgs4LeptonsFinder() = default;
  virtual bool process(HiggsFourLeptonsEvent & event) override;
};
