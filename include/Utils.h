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

const Electron::Selector ele_id = Electron::IDMVAIsoLoose;
const Muon::Selector muo_id  = Muon::IDCutBasedTrackerHighPt;
const Muon::Selector muo_iso = Muon::IsoPFLoose;

const float H_mass_reco = 125;
const float H_width_reco = 10;
const float Z_mass_reco = 91;
const float Z_width_reco = 15;
const float Z_mass_offshell_reco = 25;
const float Z_width_offshell_reco = 20;
const float highest_Z_mass_min = 40;
const float fourLeptonInvMass_min = 70;
const float fourLeptonInvMass_min_offshell = 180;
const float Z_mass_min = 4;
inline const float Z_mass_max = Z_mass_reco+2*Z_width_reco;
const float lep0_pt_min = 20;
const float lep1_pt_min = 10;
const float ghostlepton_dR_min = 0.02;


const std::vector<std::string> EventCategories = {"undefined", "multiple", "4m", "4e", "2m2e", "OS-4m", "OS-4e", "OS-2m2e"};


const std::unordered_map<std::string, std::map<std::string, std::pair<std::string, std::pair<int, int>>>>
Trigger_run_validity = {
  { "UL17", {
    { "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_*",              std::pair("DoubleEG",       std::pair(297046, 284068)) },
    { "HLT_DoubleEle33_CaloIdL_GsfTrkIdVL*",                   std::pair("DoubleEG",       std::pair(297046, 284068)) },
    { "HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL*",                std::pair("DoubleEG",       std::pair(297046, 284068)) },
    { "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8*",          std::pair("DoubleMuon",     std::pair(297046, 284068)) },
    { "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8*",            std::pair("DoubleMuon",     std::pair(297046, 284068)) },
    { "HLT_TripleMu_12_10_5*",                                 std::pair("DoubleMuon",     std::pair(297046, 284068)) },
    { "HLT_TripleMu_10_5_5_D2*",                               std::pair("DoubleMuon",     std::pair(297046, 284068)) },
    { "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL*",      std::pair("MuonEG",         std::pair(297046, 284068)) },
    { "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ*",    std::pair("MuonEG",         std::pair(297046, 284068)) },
    { "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ*",   std::pair("MuonEG",         std::pair(297046, 284068)) },
    { "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ*",   std::pair("MuonEG",         std::pair(297046, 284068)) },
    { "HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ*",                   std::pair("MuonEG",         std::pair(297046, 284068)) },
    { "HLT_Mu8_DiEle12_CaloIdL_TrackIdL*",                     std::pair("MuonEG",         std::pair(297046, 284068)) },
    { "HLT_Mu8_DiEle12_CaloIdL_TrackIdL_DZ*",                  std::pair("MuonEG",         std::pair(297046, 284068)) },
    { "HLT_Ele35_WPTight_Gsf_v*",                              std::pair("SingleElectron", std::pair(297046, 284068)) },
    { "HLT_Ele38_WPTight_Gsf_v*",                              std::pair("SingleElectron", std::pair(297046, 284068)) },
    { "HLT_Ele40_WPTight_Gsf_v*",                              std::pair("SingleElectron", std::pair(297046, 284068)) },
    { "HLT_IsoMu27*",                                          std::pair("SingleMuon",     std::pair(297046, 284068)) },
  }},
  { "UL18", {
    { "HLT_IsoMu24_v*",                                        std::pair("SingleMuon",     std::pair(315252, 325175)) },
    { "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*", std::pair("SingleMuon",     std::pair(315252, 325175)) },
    { "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v*",             std::pair("DoubleEG",       std::pair(315252, 325175)) },
    { "HLT_DoubleEle25_CaloIdL_MW_v*",                         std::pair("DoubleEG",       std::pair(315252, 325175)) },
    { "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v*",        std::pair("DoubleMuon",     std::pair(315252, 325175)) },
    { "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*",    std::pair("MuonEG",         std::pair(315252, 325175)) },
    { "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*",  std::pair("MuonEG",         std::pair(315252, 325175)) },
    { "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*", std::pair("MuonEG",         std::pair(315252, 325175)) },
    { "HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v*",                 std::pair("MuonEG",         std::pair(315252, 325175)) },
    { "HLT_Ele32_WPTight_Gsf_v*",                              std::pair("SingleElectron", std::pair(315252, 325175)) },
    { "HLT_IsoMu24_v*",                                        std::pair("SingleMuon",     std::pair(315252, 325175)) },
  }},
};
