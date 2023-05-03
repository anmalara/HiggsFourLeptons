#include <iostream>

#include "LEAF/Analyzer/include/BaseTool.h"
#include "LEAF/Analyzer/include/JetHists.h"
#include "LEAF/Analyzer/include/MuonHists.h"
#include "LEAF/Analyzer/include/ElectronHists.h"
#include "LEAF/Analyzer/include/JetIds.h"
#include "LEAF/Analyzer/include/MuonIds.h"
#include "LEAF/Analyzer/include/ElectronIds.h"
#include "LEAF/Analyzer/include/NElectronSelection.h"
#include "LEAF/Analyzer/include/NMuonSelection.h"
#include "LEAF/Analyzer/include/NJetSelection.h"
#include "LEAF/Analyzer/include/FlagSelection.h"
#include "LEAF/Analyzer/include/LumiWeightApplicator.h"

#include "LEAF/HiggsFourLeptons/include/Utils.h"
#include "LEAF/HiggsFourLeptons/include/HiggsFourLeptonsEvent.h"
#include "LEAF/HiggsFourLeptons/include/HiggsFourLeptonsHists.h"
#include "LEAF/HiggsFourLeptons/include/Higgs4LeptonsFinder.h"

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
  "Higgs4LeptonsReco", "Higgs4Leptons_Selection", "nominal"};

  unordered_map<string, string> input_strings;
  unordered_map<string, bool> input_bools;
  // Modules used in the analysis
  unique_ptr<LumiWeightApplicator> lumiweight_applicator;
  unique_ptr<MuonCleaner> muo_cleaner;
  unique_ptr<ElectronCleaner> ele_cleaner;
  unique_ptr<JetCleaner> jet_cleaner;
  unique_ptr<PFCandCleaner> pfcand_cleaner;

  // Selections used in the analysis
  unique_ptr<NElectronSelection> nele_selection;
  unique_ptr<NMuonSelection> nmuo_selection;
  unique_ptr<NJetSelection> njets_selection;
  unique_ptr<Higgs4LeptonsFinder> Higgs4Leptons_finder;

  unordered_map<string, unique_ptr<FlagSelection>> Trigger_selection;
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
    mytag = tag+"_Jets";      book_HistFolder(mytag, new JetHists(mytag));
    mytag = tag+"_Muons";     book_HistFolder(mytag, new MuonHists(mytag));
    mytag = tag+"_Electrons"; book_HistFolder(mytag, new ElectronHists(mytag));
    mytag = tag+"_H4l";       book_HistFolder(mytag, new HiggsFourLeptonsHists(mytag));
  }
}

void HiggsFourLeptonsTool::fill_histograms(TString tag){
  TString mytag;
  mytag = tag+"_Jets";      HistFolder<JetHists>(mytag)->fill(*event);
  mytag = tag+"_Muons";     HistFolder<MuonHists>(mytag)->fill(*event);
  mytag = tag+"_Electrons"; HistFolder<ElectronHists>(mytag)->fill(*event);
  mytag = tag+"_H4l";       HistFolder<HiggsFourLeptonsHists>(mytag)->fill(*event);

}



HiggsFourLeptonsTool::HiggsFourLeptonsTool(const Config & cfg) : BaseTool(cfg){

  input_strings["name"] = cfg.dataset_name();
  input_strings["type"] = cfg.dataset_type();
  input_strings["year"] = cfg.dataset_year();
  PrintInputs();

  event = new HiggsFourLeptonsEvent();
  event->reset();

  lumiweight_applicator.reset(new LumiWeightApplicator(cfg));

  MultiID<Muon> muo_ID = {PtEtaId(muo_pt_min, muo_eta_min), MuonID(muo_id), MuonID(muo_iso)};
  MultiID<Electron> ele_ID = {PtEtaId(ele_pt_min, ele_eta_min), ElectronDetectorHolesID(), ElectronID(ele_id)};

  muo_cleaner.reset(new MuonCleaner(muo_ID));
  ele_cleaner.reset(new ElectronCleaner(ele_ID));

  MultiID<Jet> jet_id = {PtEtaId(jet_pt_min,jet_eta_min), JetID(JetID::WP_TIGHT), JetPUID(JetPUID::WP_TIGHT), JetLeptonOverlapID(0.4)};
  jet_cleaner.reset(new JetCleaner(jet_id));

  MultiID<PFCandidate> pfcand_id = {PtEtaId(0.2, 5.2)};
  pfcand_cleaner.reset(new PFCandCleaner(pfcand_id));

  // nele_selection.reset(new NElectonSelection(cfg, , -1));
  // nmuo_selection.reset(new NMuonSelection(cfg, 1, -1));
  // njets_selection.reset(new NJetSelection(cfg, 1, -1));

  Higgs4Leptons_finder.reset(new Higgs4LeptonsFinder(cfg));

  for (auto& t : Trigger_run_validity.at(input_strings["year"])) {
    if (input_strings["type"]=="DATA" && !FindInString(t.second.first,input_strings["name"])) continue;
    Trigger_selection[t.first].reset(new FlagSelection(cfg, t.first ));
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

  lumiweight_applicator->process(*event);
  fill_histograms("weights");

  bool pass_triggers_OR = false;
  for (auto& el : Trigger_selection) {
    // if (event.isRealData && (event.run < Trigger_run_validity.at(input_strings["year"]).at(el.first).first || event.run > Trigger_run_validity.at(input_strings["year"]).at(el.first).second) ) continue;
    pass_triggers_OR += el.second->passes(*event);
    if (pass_triggers_OR) break;
  }
  if (!pass_triggers_OR) return false;

  fill_histograms("triggers");

  clean_objects();
  fill_histograms("clean");

  bool pass_H4l = Higgs4Leptons_finder->process(*event);
  fill_histograms("Higgs4LeptonsReco");
  if(!pass_H4l) return false;
  fill_histograms("Higgs4Leptons_Selection");

  // fill one set of histograms called "nominal", which is necessary for PostAnalyzer scripts
  fill_histograms("nominal");

  // store events passing the full selection for the next step
  return true;
}




REGISTER_TOOL(HiggsFourLeptonsTool)
