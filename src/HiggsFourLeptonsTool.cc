#include <iostream>

#include "LEAF/Analyzer/include/BaseTool.h"
#include "LEAF/Analyzer/include/JetHists.h"
#include "LEAF/Analyzer/include/MuonHists.h"
#include "LEAF/Analyzer/include/ElectronHists.h"
#include "LEAF/Analyzer/include/TauHists.h"
#include "LEAF/Analyzer/include/JetIds.h"
#include "LEAF/Analyzer/include/MuonIds.h"
#include "LEAF/Analyzer/include/ElectronIds.h"
#include "LEAF/Analyzer/include/TauIds.h"
#include "LEAF/Analyzer/include/NJetSelection.h"
#include "LEAF/Analyzer/include/NTauSelection.h"
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
  vector<string> histogram_tags = {"input", "weights", "notau_Selection",
  "NObject_Selection", "phasespace_Selection", "Higgs4LeptonsReco", "Higgs4Leptons_Selection",
  "nominal"};

  unordered_map<string, string> input_strings;
  unordered_map<string, bool> input_bools;
  // Modules used in the analysis
  unique_ptr<LumiWeightApplicator> lumiweight_applicator;
  unique_ptr<MuonCleaner> muo_cleaner;
  unique_ptr<ElectronCleaner> ele_cleaner;
  unique_ptr<TauCleaner> tau_cleaner;
  unique_ptr<JetCleaner> jet_cleaner;
  unique_ptr<PFCandCleaner> pfcand_cleaner;

  // Selections used in the analysis
  unique_ptr<NJetSelection> njets_selection;
  unique_ptr<NTauSelection> ntaus_selection;
  unique_ptr<Higgs4LeptonsFinder> Higgs4Leptons_finder;
};


void HiggsFourLeptonsTool::PrintInputs() {
  cout << blue << string(40, '*' ) << reset << endl;
  PrintHeader(NameTool);
  for (auto x : input_strings) cout << x.first << string( 18-x.first.size(), ' ' ) << x.second << '\n';
  for (auto x : input_bools)   cout << x.first << string( 18-x.first.size(), ' ' ) << BoolToTString(x.second) << '\n';
  cout << blue << string(40, '*' ) << reset << endl;
}

void HiggsFourLeptonsTool::book_histograms(){
  for(const TString & tag : histogram_tags){
    TString mytag;
    mytag = tag+"_Jets"; book_HistFolder(mytag, new JetHists(mytag));
    mytag = tag+"_H4l";  book_HistFolder(mytag, new HiggsFourLeptonsHists(mytag));
  }
}

void HiggsFourLeptonsTool::fill_histograms(TString tag){
  TString mytag;
  mytag = tag+"_Jets";   HistFolder<JetHists>(mytag)->fill(*event);
  mytag = tag+"_H4l";    HistFolder<HiggsFourLeptonsHists>(mytag)->fill(*event);

}



HiggsFourLeptonsTool::HiggsFourLeptonsTool(const Config & cfg) : BaseTool(cfg){

  event = new HiggsFourLeptonsEvent();
  event->reset();

  lumiweight_applicator.reset(new LumiWeightApplicator(cfg));

  MultiID<Muon> muon_id_base = {PtEtaId(3, 2.5)};
  MultiID<Electron> electron_id_base = {PtEtaId(5, 2.5), ElectronDetectorHolesID()};
  MultiID<Muon> muo_id = {muon_id_base, MuonID(Muon::IDCutBasedLoose), MuonID(Muon::IsoPFLoose)};
  MultiID<Electron> ele_id = {electron_id_base, ElectronID(Electron::IDMVAIsoLoose)};

  muo_cleaner.reset(new MuonCleaner(muo_id));
  ele_cleaner.reset(new ElectronCleaner(ele_id));

  MultiID<Jet> jet_id = {PtEtaId(20, 5.2), JetID(JetID::WP_TIGHT), JetPUID(JetPUID::WP_TIGHT), JetLeptonOverlapID(0.4)};
  jet_cleaner.reset(new JetCleaner(jet_id));

  MultiID<PFCandidate> pfcand_id = {PtEtaId(0.2, 5.2)};
  pfcand_cleaner.reset(new PFCandCleaner(pfcand_id));

  njets_selection.reset(new NJetSelection(cfg, 1, -1));
  ntaus_selection.reset(new NTauSelection(cfg, -1, 0));


  Higgs4Leptons_finder.reset(new Higgs4LeptonsFinder(cfg));

  book_histograms();
  PrintInputs();
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
  tau_cleaner->process(*event);
  jet_cleaner->process(*event);
  pfcand_cleaner->process(*event);
}

bool HiggsFourLeptonsTool::select_Nobjects(){
  // if (event->genjets->size()<2) return false;
  if(!njets_selection->passes(*event)) return false;
  return true;
}

bool HiggsFourLeptonsTool::Process(){

  sort_objects();
  fill_histograms("input");

  lumiweight_applicator->process(*event);
  fill_histograms("weights");

  clean_objects();
  if(!ntaus_selection->passes(*event)) return false;
  fill_histograms("notau_Selection");

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
