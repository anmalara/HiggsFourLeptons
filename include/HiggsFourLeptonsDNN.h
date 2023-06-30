#pragma once

#include "LEAF/Analyzer/include/Config.h"
#include "LEAF/Analyzer/include/AnalysisModule.h"
#include "LEAF/HiggsFourLeptons/include/HiggsFourLeptonsEvent.h"
#include "PhysicsTools/ONNXRuntime/interface/ONNXRuntime.h"

class HiggsFourLeptonsDNN: public AnalysisModule<HiggsFourLeptonsEvent> {
public:
  explicit HiggsFourLeptonsDNN(const Config& cfg);
  virtual ~HiggsFourLeptonsDNN() = default;
  virtual bool process(HiggsFourLeptonsEvent & event) override;

  std::unique_ptr<cms::Ort::ONNXRuntime> ONNX_inference;

};
