#include "LEAF/Analyzer/include/constants.h"
#include "LEAF/Analyzer/include/useful_functions.h"

#include "LEAF/HiggsFourLeptons/include/Utils.h"
#include "LEAF/HiggsFourLeptons/include/HiggsFourLeptonsHists.h"

using namespace std;

HiggsFourLeptonsHists::HiggsFourLeptonsHists(TString dir_) : BaseHists(dir_){

  book<TH1F>("sumweights",        ";sum of event weights; Events / bin",   1,       0.5,     1.5);
  book<TH1F>("eventCategory",     ";eventCategory; Events / bin", EventCategories.size(), 0., EventCategories.size());
  book<TH1F>("number_ele",        ";number of electrons ; Events / bin",  11,      -0.5,    10.5);
  book<TH1F>("number_muo",        ";number of muons ; Events / bin",      11,      -0.5,    10.5);
  book<TH1F>("number_lep",        ";number of leptons ; Events / bin",    11,      -0.5,    10.5);
  book<TH2F>("number_elevsmuo",   ";number of electrons; number of muons", 5,      -0.5,     4.5,     5,      -0.5,    4.5);
  book<TH1F>("number_Z",          ";number of Z bosons ; Events / bin",   11,      -0.5,    10.5);
  book<TH1F>("number_H",          ";number of H bosons ; Events / bin",   11,      -0.5,    10.5);

  for (unsigned int i=0;i<EventCategories.size();i++) {
    hist<TH1F>("eventCategory")->GetXaxis()->SetBinLabel(i+1,EventCategories[i].c_str());
  }

  for (const TString& name: {"H", "Z1", "Z2", "H_else", "Z_else"}){
    book<TH1F>(name+"_pt",       ";p_{T,"+name+"}; Events / bin",        100,       0.,    500);
    book<TH1F>(name+"_eta",      ";#eta_{"+name+"}; Events / bin",       100,      -5.0,     5.0);
    book<TH1F>(name+"_phi",      ";#phi_{"+name+"}; Events / bin",       100,      -4.0,     4.0);
    book<TH1F>(name+"_mass",     ";mass_{"+name+"}; Events / bin",        50,      70,     170.0);
    book<TH1F>(name+"_mass_ext", ";mass_{"+name+"}; Events / bin",       100,     170,    1170.0);
  }

  max_index = 5;
  for (const TString& lep: {"ele", "muo", "lep"}){
    TString name;
    for(int i=1; i<=max_index; i++){
      name = lep+to_string(i);
      book<TH1F>(name+"_pt",       ";#p_{T, "+name+"}; Events / bin",    100,       0.,    500/i);
      book<TH1F>(name+"_eta",      ";#eta_{"+name+"}; Events / bin",     100,      -5.0,     5.0);
      book<TH1F>(name+"_phi",      ";#phi_{"+name+"}; Events / bin",     100,      -4.0,     4.0);
    }
    name = lep+"1vs"+lep+"2";
    book<TH2F>(name+"_pt",          ";#p_{T,"+lep+"1};#p_{T,"+lep+"2}",   50,       0.,   1000,     50,       0.,  1000);
    book<TH2F>(name+"_eta",         ";#eta_{"+lep+"1};#eta_{"+lep+"2}",  100,      -5.0,     5.0,  100,      -5.0,    5.0);
    book<TH2F>(name+"_eta_abs",     ";#eta_{"+lep+"1};#eta_{"+lep+"2}",  100,      -0.0,     5.0,  100,      -0.0,    5.0);
  }

}

void HiggsFourLeptonsHists::fill(const HiggsFourLeptonsEvent & event){
  double weight = event.weight;
  hist<TH1F>("sumweights")->Fill(1, weight);
  hist<TH1F>("eventCategory")->Fill(event.eventCategory().c_str(), weight);

  int ele_size = (*event.H_electrons).size();
  int muo_size = (*event.H_muons).size();
  int lep_size = (*event.H_leptons).size();
  int Z_size = (*event.reco_Z_bosons).size();
  int H_size = (*event.reco_H_bosons).size();

  hist<TH1F>("number_ele")->Fill(ele_size, weight);
  hist<TH1F>("number_muo")->Fill(muo_size, weight);
  hist<TH1F>("number_lep")->Fill(lep_size, weight);
  hist<TH2F>("number_elevsmuo")->Fill(ele_size, muo_size, weight);
  hist<TH1F>("number_Z")->Fill(Z_size, weight);
  hist<TH1F>("number_H")->Fill(H_size, weight);


  for(int i=0; i<Z_size; i++){
    TLorentzVector boson = (*event.reco_Z_bosons).at(i);
    TString name = "Z"; name += ((i<2)? to_string((i+1)) : "_else");
    hist<TH1F>(name+"_pt")->Fill(boson.Pt(), weight);
    hist<TH1F>(name+"_eta")->Fill(boson.Eta(), weight);
    hist<TH1F>(name+"_phi")->Fill(boson.Phi(), weight);
    hist<TH1F>(name+"_mass")->Fill(boson.M(), weight);
    hist<TH1F>(name+"_mass_ext")->Fill(boson.M(), weight);
  }

  for(int i=0; i<H_size; i++){
    TLorentzVector boson = (*event.reco_H_bosons).at(i);
    TString name = "H"; name += ((i<1)? "" : "_else");
    hist<TH1F>(name+"_pt")->Fill(boson.Pt(), weight);
    hist<TH1F>(name+"_eta")->Fill(boson.Eta(), weight);
    hist<TH1F>(name+"_phi")->Fill(boson.Phi(), weight);
    hist<TH1F>(name+"_mass")->Fill(boson.M(), weight);
    hist<TH1F>(name+"_mass_ext")->Fill(boson.M(), weight);
  }

  for(int i=0; i<ele_size; i++){
    TString postfix = (i>=max_index)? to_string(max_index) : to_string(i+1);
    const Electron ele = (*event.H_electrons).at(i);
    hist<TH1F>("ele"+postfix+"_pt")->Fill(ele.pt(), weight);
    hist<TH1F>("ele"+postfix+"_eta")->Fill(ele.eta(), weight);
    hist<TH1F>("ele"+postfix+"_phi")->Fill(ele.phi(), weight);
    if (i>=1) continue;
    const Electron ele2 = (*event.H_electrons).at(i+1);
    hist<TH2F>("ele1vsele2_pt")->Fill(ele.pt(), ele2.pt(), weight);
    hist<TH2F>("ele1vsele2_eta")->Fill(ele.eta(), ele2.eta(), weight);
    hist<TH2F>("ele1vsele2_eta_abs")->Fill(fabs(ele.eta()), fabs(ele2.eta()), weight);
  }

  for(int i=0; i<muo_size; i++){
    TString postfix = (i>=max_index)? to_string(max_index) : to_string(i+1);
    const Muon muo = (*event.H_muons).at(i);
    hist<TH1F>("muo"+postfix+"_pt")->Fill(muo.pt(), weight);
    hist<TH1F>("muo"+postfix+"_eta")->Fill(muo.eta(), weight);
    hist<TH1F>("muo"+postfix+"_phi")->Fill(muo.phi(), weight);
    if (i>=1) continue;
    const Muon muo2 = (*event.H_muons).at(i+1);
    hist<TH2F>("muo1vsmuo2_pt")->Fill(muo.pt(), muo2.pt(), weight);
    hist<TH2F>("muo1vsmuo2_eta")->Fill(muo.eta(), muo2.eta(), weight);
    hist<TH2F>("muo1vsmuo2_eta_abs")->Fill(fabs(muo.eta()), fabs(muo2.eta()), weight);
  }

  for(int i=0; i<lep_size; i++){
    TString postfix = (i>=max_index)? to_string(max_index) : to_string(i+1);
    const FlavorParticle lep = (*event.H_leptons).at(i);
    hist<TH1F>("lep"+postfix+"_pt")->Fill(lep.pt(), weight);
    hist<TH1F>("lep"+postfix+"_eta")->Fill(lep.eta(), weight);
    hist<TH1F>("lep"+postfix+"_phi")->Fill(lep.phi(), weight);
    if (i>=1) continue;
    const FlavorParticle lep2 = (*event.H_leptons).at(i+1);
    hist<TH2F>("lep1vslep2_pt")->Fill(lep.pt(), lep2.pt(), weight);
    hist<TH2F>("lep1vslep2_eta")->Fill(lep.eta(), lep2.eta(), weight);
    hist<TH2F>("lep1vslep2_eta_abs")->Fill(fabs(lep.eta()), fabs(lep2.eta()), weight);
  }

}
