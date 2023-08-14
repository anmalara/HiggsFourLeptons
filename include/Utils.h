#pragma once

#include <iostream>
#include <string.h>
#include <unordered_map>

#include "TString.h"

#include "LEAF/Analyzer/include/RecoEvent.h"
#include "LEAF/Analyzer/include/useful_functions.h"

inline const TString BoolToTString(bool b) { return b ? "true" : "false";}
void PrintHeader(TString header, int max_lenght = 40, TString color="blue");


const float ele_pt_min = 7;
const float muo_pt_min = 5;
const float jet_pt_min = 30;

const float ele_eta_min = 2.5;
const float muo_eta_min = 2.4;
const float jet_eta_min = 4.7;

const float lep_dxy_min = 0;
const float lep_dxy_max = 0.5;
const float lep_dz_min = 0;
const float lep_dz_max = 1;

const Electron::Selector ele_id = Electron::IDMVAIsoLoose;
const Muon::Selector muo_id  = Muon::IDCutBasedTight; //IDCutBasedLoose
const Muon::Selector muo_iso = Muon::IsoPFLoose;

const float H_mass_reco = 125;
const float H_width_reco = 10;
const float Z_mass_reco = 91;
const float Z_width_reco = 15;
const float Z_mass_offshell_reco = 25;
const float Z_width_offshell_reco = 20;
const float highest_Z_mass_min = 40;
const float lower_Z_mass_min = 12;
const float fourLeptonInvMass_min = 70;
const float fourLeptonInvMass_min_offshell = 180;
const float Z_mass_min = 4;
inline const float Z_mass_max = Z_mass_reco+2*Z_width_reco;
const float lep0_pt_min = 20;
const float lep1_pt_min = 10;
const float ghostlepton_dR_min = 0.02;
const float cross_cleaning_dR_min = 0.05;

const float muo_iso_rel_03_min = 0.35;
const float ele_iso_rel_03_min = 0.2;


const std::vector<std::string> EventCategories = {"undefined", "multiple", "4m", "4e", "2m2e", "OS-4m", "OS-4e", "OS-2m2e"};


const std::unordered_map<std::string, std::map<std::string, std::map<std::string, std::vector<std::string> >>>
Trigger_map = {
  { "UL18", {
    {"MC", 
    {
      {"Pass", {"HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*",
                "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v*",
                "HLT_IsoMu24_v*",
                "HLT_IsoTkMu24_v*",
                "HLT_IsoMu27_v*",
                "HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*",
                "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*",
                "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v*",
                "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*",
                "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v*",
                "HLT_Ele27_WPTight_Gsf_v*",
                "HLT_Ele32_WPTight_Gsf_v*",
                "HLT_Ele35_WPTight_Gsf_v*",
                "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v*"}},
      {"Fail", {}},
    }
    },
    {"EGamma", 
    {
      {"Pass", {"HLT_Ele27_WPTight_Gsf_v*",
                "HLT_Ele32_WPTight_Gsf_v*",
                "HLT_Ele35_WPTight_Gsf_v*",
                "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v*"}},
      {"Fail", {"HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*",
                "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v*",
                "HLT_IsoMu24_v*",
                "HLT_IsoTkMu24_v*",
                "HLT_IsoMu27_v*",
                "HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*",
                "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*",
                "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v*",
                "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*",
                "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v*"}},
    }
    },
    {"DoubleMuon", 
    {
      {"Pass", {"HLT_TkMu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*",
                "HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ_v*",
                "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v*",
                "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*",
                "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v*"}},
      {"Fail", {"HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*",
                "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v*",
                "HLT_IsoMu24_v*",
                "HLT_IsoTkMu24_v*",
                "HLT_IsoMu27_v*"}},
    }
    },
    {"MuonEG", 
    {
      {"Pass", {"HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*",
                "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v*"}},
      {"Fail", {}},
    }
    },
    {"SingleMuon", 
    {
      {"Pass", {"HLT_IsoMu24_v*",
                "HLT_IsoTkMu24_v*",
                "HLT_IsoMu27_v*"}},
      {"Fail", {"HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*",
                "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v*"}},
    }
    }
    }
  }
  };
