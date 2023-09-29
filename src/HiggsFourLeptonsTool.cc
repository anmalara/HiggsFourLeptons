#include <iostream>

#include "LEAF/Analyzer/include/BaseTool.h"
#include "LEAF/Analyzer/include/EventHists.h"
#include "LEAF/Analyzer/include/JetHists.h"
#include "LEAF/Analyzer/include/MuonHists.h"
#include "LEAF/Analyzer/include/ElectronHists.h"
#include "LEAF/Analyzer/include/TauHists.h"
#include "LEAF/Analyzer/include/JetIds.h"
#include "LEAF/Analyzer/include/MuonIds.h"
#include "LEAF/Analyzer/include/ElectronIds.h"
#include "LEAF/Analyzer/include/TauIds.h"
#include "LEAF/Analyzer/include/NElectronSelection.h"
#include "LEAF/Analyzer/include/NMuonSelection.h"
#include "LEAF/Analyzer/include/NJetSelection.h"
#include "LEAF/Analyzer/include/FlagSelection.h"
#include "LEAF/Analyzer/include/LumiWeightApplicator.h"
#include "LEAF/Analyzer/include/LumiblockSelection.h"

#include "LEAF/HiggsFourLeptons/include/Utils.h"
#include "LEAF/HiggsFourLeptons/include/HiggsFourLeptonsEvent.h"
#include "LEAF/HiggsFourLeptons/include/HiggsFourLeptonsHists.h"
#include "LEAF/HiggsFourLeptons/include/Higgs4LeptonsFinder.h"

#include "LEAF/HiggsFourLeptons/include/HiggsFourLeptonsDNN.h"
#include "LEAF/HiggsFourLeptons/include/HiggsFourLeptonsDNNHists.h"
#include <iostream>

using namespace std;

class HiggsFourLeptonsTool : public BaseTool {

public:
  // Constructors, destructor
  HiggsFourLeptonsTool(const Config & cfg);
  ~HiggsFourLeptonsTool() = default;
  void ProcessDataset(const Config & cfg) override {LoopEvents<HiggsFourLeptonsTool, HiggsFourLeptonsEvent>(cfg, event, *this);};
  virtual bool Process() override;
  void book_histograms();
  void fill_histograms(TString);
  void PrintInputs();
  void sort_objects();
  void clean_objects();
  bool select_Nobjects();


private:
  HiggsFourLeptonsEvent* event;

  string NameTool = "HiggsFourLeptonsTool";
  vector<string> histogram_tags = {"input", "weights", "triggers", "clean",
  "Higgs4LeptonsReco", "Higgs4Leptons_Selection","nominal","Z1_lowM",
  "Z1_recoM_Z2_lowM","Z1_recoM_Z2_recoM","4e","4m","2m2e","H_m_reco", "Z_m_reco","H_m_geq_180"};

  unordered_map<string, string> input_strings;
  unordered_map<string, bool> input_bools;
  // Modules used in the analysis
  unique_ptr<LumiWeightApplicator> lumiweight_applicator;
  unique_ptr<LumiblockSelection> lumiblock_selection;
  unique_ptr<MuonCleaner> muo_cleaner;
  unique_ptr<ElectronCleaner> ele_cleaner;
  unique_ptr<JetCleaner> jet_cleaner;
  unique_ptr<TauCleaner> tau_cleaner;
  unique_ptr<PFCandCleaner> pfcand_cleaner;

  // Selections used in the analysis
  unique_ptr<NElectronSelection> nele_selection;
  unique_ptr<NMuonSelection> nmuo_selection;
  unique_ptr<NJetSelection> njets_selection;
  unique_ptr<Higgs4LeptonsFinder> Higgs4Leptons_finder;
  unique_ptr<HiggsFourLeptonsDNN> DNN_module;
  
  unordered_map<string, unique_ptr<FlagSelection>> Trigger_selection;
  unordered_map<string, unique_ptr<FlagSelection>> Trigger_selection_pass;
  unordered_map<string, unique_ptr<FlagSelection>> Trigger_selection_fail;
};


void HiggsFourLeptonsTool::PrintInputs() {
  cout << blue << string(40, '*' ) << reset << endl;
  PrintHeader(NameTool);
  for (auto x : input_strings) cout << blue << x.first << string( 18-x.first.size(), ' ' ) << x.second << '\n';
  for (auto x : input_bools)   cout << blue << x.first << string( 18-x.first.size(), ' ' ) << BoolToTString(x.second) << '\n';
  cout << blue << string(40, '*' ) << reset << endl;
}

void HiggsFourLeptonsTool::book_histograms(){
  for(const TString & tag : histogram_tags){
    TString mytag;

    // mytag = tag+"_Event";     book_HistFolder(mytag, new EventHists(mytag));
    mytag = tag+"_Jets";      book_HistFolder(mytag, new JetHists(mytag));
    // mytag = tag+"_Muons";     book_HistFolder(mytag, new MuonHists(mytag));
    // mytag = tag+"_Electrons"; book_HistFolder(mytag, new ElectronHists(mytag));
    // mytag = tag+"_Taus";      book_HistFolder(mytag, new TauHists(mytag));
    mytag = tag+"_H4l";       book_HistFolder(mytag, new HiggsFourLeptonsHists(mytag));
    mytag = tag+ "_PF";         book_HistFolder(mytag, new HiggsFourLeptonsDNNHists(mytag));
  }
}

void HiggsFourLeptonsTool::fill_histograms(TString tag){
  TString mytag;
  // mytag = tag+"_Event";     HistFolder<EventHists>(mytag)->fill(*event);
  mytag = tag+"_Jets";      HistFolder<JetHists>(mytag)->fill(*event);
  // mytag = tag+"_Muons";     HistFolder<MuonHists>(mytag)->fill(*event);
  // mytag = tag+"_Electrons"; HistFolder<ElectronHists>(mytag)->fill(*event);
  // mytag = tag+"_Taus";      HistFolder<TauHists>(mytag)->fill(*event);
  mytag = tag+"_H4l";       HistFolder<HiggsFourLeptonsHists>(mytag)->fill(*event);
  mytag = tag+"_PF";        HistFolder<HiggsFourLeptonsDNNHists>(mytag)->fill(*event);

}



HiggsFourLeptonsTool::HiggsFourLeptonsTool(const Config & cfg) : BaseTool(cfg){

  DNN_module.reset(new  HiggsFourLeptonsDNN(cfg));

  input_strings["name"] = cfg.dataset_name();
  input_strings["type"] = cfg.dataset_type();
  input_strings["year"] = cfg.dataset_year();
  PrintInputs();

  event = new HiggsFourLeptonsEvent();
  event->reset();

  lumiweight_applicator.reset(new LumiWeightApplicator(cfg));
  lumiblock_selection.reset(new LumiblockSelection(cfg));

  MultiID<Muon> muo_ID = {PtEtaId(muo_pt_min, muo_eta_min), 
                          MuonDxyID(lep_dxy_min,lep_dxy_max), 
                          MuonDzID(lep_dz_min,lep_dz_max), 
                          MuonID(muo_id),    
                          MuonIso(muo_iso_rel_03_min,"iso_rel_03"),
                          MuonIso(muo_iso_rel_03_min,"iso_rel_03_charged")};//MuonIso(,"iso_rel_04"),MuonIso(,"iso_tk")

  MultiID<Electron> ele_ID = {PtEtaId(ele_pt_min, ele_eta_min), 
                              ElectronDetectorHolesID(), 
                              ElectronDxyID(lep_dxy_min,lep_dxy_max),
                              ElectronDzID(lep_dz_min,lep_dz_max),
                              ElectronID(ele_id),
                              ElectronIso(ele_iso_rel_03_min,"iso_rel_03")};//ElectronIso(ele_iso_rel_03_min,"iso_rel_03_charged")

  muo_cleaner.reset(new MuonCleaner(muo_ID));
  ele_cleaner.reset(new ElectronCleaner(ele_ID));

  MultiID<Jet> jet_id = {PtEtaId(jet_pt_min,jet_eta_min), JetID(JetID::WP_TIGHT), JetPUID(JetPUID::WP_TIGHT), JetLeptonOverlapID(0.4)};
  jet_cleaner.reset(new JetCleaner(jet_id));

  MultiID<Tau> tau_id = {TauID(Tau::DeepTauVsJetVVVLoose), TauID(Tau::DeepTauVsEleVVVLoose), TauID(Tau::DeepTauVsMuVLoose)};
  tau_cleaner.reset(new TauCleaner(tau_id));

  MultiID<PFCandidate> pfcand_id = {PtEtaId(0.2, 5.2)};
  pfcand_cleaner.reset(new PFCandCleaner(pfcand_id));

  // nele_selection.reset(new NElectonSelection(cfg, , -1));
  // nmuo_selection.reset(new NMuonSelection(cfg, 1, -1));
  // njets_selection.reset(new NJetSelection(cfg, 1, -1));

  Higgs4Leptons_finder.reset(new Higgs4LeptonsFinder(cfg));

  std::vector<std::string> Pass_require = Trigger_map.at(input_strings["year"]).at("MC").at("Pass");
  std::vector<std::string> Fail_require = Trigger_map.at(input_strings["year"]).at("MC").at("Fail");
  
  if (input_strings["type"]=="DATA") {
    for (auto& t : Trigger_map.at(input_strings["year"])) {
      if (!FindInString(t.first,input_strings["name"])) continue;
      Pass_require = t.second.at("Pass");
      Fail_require = t.second.at("Fail");
  }
  }

  for (auto& t : Pass_require) {
      Trigger_selection_pass[t].reset(new FlagSelection(cfg, t));
  }

  for (auto& t : Fail_require) {
      Trigger_selection_fail[t].reset(new FlagSelection(cfg, t));
  }

  book_histograms();
}


void HiggsFourLeptonsTool::sort_objects(){
  sort_by_pt<GenParticle>(*event->genparticles_stable);
  sort_by_pt<GenJet>(*event->genjets);
  sort_by_pt<Jet>(*event->jets_ak4chs);
  sort_by_pt<PFCandidate>(*event->pfcands);
}

void HiggsFourLeptonsTool::clean_objects(){
  muo_cleaner->process(*event);
  ele_cleaner->process(*event);
  jet_cleaner->process(*event);
  tau_cleaner->process(*event);
  pfcand_cleaner->process(*event);
}

bool HiggsFourLeptonsTool::select_Nobjects(){
  // // if (event->genjets->size()<2) return false;
  // if(!nele_selection->passes(*event)) return false;
  // if(!nmuo_selection->passes(*event)) return false;
  // if(!njets_selection->passes(*event)) return false;
  return true;
}

bool HiggsFourLeptonsTool::Process(){
  sort_objects();
  fill_histograms("input");

  bool pass_lumi_selection = lumiblock_selection->passes(*event);
  if (!pass_lumi_selection) return false;
  lumiweight_applicator->process(*event);
  fill_histograms("weights");

  bool pass_triggers_OR = false;
  for (auto& el : Trigger_selection_pass) {
    pass_triggers_OR += el.second->passes(*event);
  }
  if (!pass_triggers_OR) return false;

  bool fail_triggers_OR = false;
  for (auto& el : Trigger_selection_fail) {
    fail_triggers_OR += el.second->passes(*event);
  }

  if (fail_triggers_OR){
    return false;
  }

  fill_histograms("triggers");

  clean_objects();
  fill_histograms("clean");
  bool pass_H4l = Higgs4Leptons_finder->process(*event);

  DNN_module->process(*event);
  fill_histograms("Higgs4LeptonsReco");
  if(!pass_H4l) return false;
  fill_histograms("Higgs4Leptons_Selection");
  TLorentzVector z1 = (*event->reco_Z_bosons).at(0);
  TLorentzVector z2 = (*event->reco_Z_bosons).at(1);

  if(z1.M()<80) fill_histograms("Z1_lowM");
  if(((80<z1.M())&&(z1.M()<100))&&(z2.M()<60)) fill_histograms("Z1_recoM_Z2_lowM");
  if(((80<z1.M())&&(z1.M()<100))&&((60<z2.M())&&(z2.M()<100))) fill_histograms("Z1_recoM_Z2_recoM");
  std::vector<string> eventTypes = {"4e","4m","2m2e"};
  for(size_t i=0;i<eventTypes.size();i++){
    string eventLabel = eventTypes[i];
    size_t found = (event->eventCategory()).find(eventLabel);
    if(found!=string::npos){
      fill_histograms(eventLabel);
    }
  }
  for(size_t i=0;i<(*event->reco_H_bosons).size();i++){
    TLorentzVector h = (*event->reco_H_bosons).at(i);
    if((h.M()>120)&&(h.M()<130)){
      fill_histograms("H_m_reco");
    }
    if(h.M()>180){
      fill_histograms("H_m_geq_180");
    }
    if((h.M()>81)&&(h.M()<101)){
      fill_histograms("Z_m_reco");
    }
  }
  // fill one set of histograms called "nominal", which is necessary for PostAnalyzer scripts
  fill_histograms("nominal");
  // store events passing the full selection for the next step
  return true;
}




REGISTER_TOOL(HiggsFourLeptonsTool)
