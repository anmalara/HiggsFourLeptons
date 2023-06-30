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
    std::string label = EventCategories[i];
    if (label=="undefined") label = "undef.";
    if (label=="multiple") label = ">4l";
    hist<TH1F>("eventCategory")->GetXaxis()->SetBinLabel(i+1,label.c_str());
  }

    for (const TString& name: {"H", "Z1", "Z2"}){
    book<TH1F>(name+"_pt",       ";p_{T,"+name+"}; Events / bin",        100,       0.,    500);
    book<TH1F>(name+"_eta",      ";#eta_{"+name+"}; Events / bin",       100,      -5.0,     5.0);
    book<TH1F>(name+"_phi",      ";#phi_{"+name+"}; Events / bin",       100,      -4.0,     4.0);
    if (FindInString("H", name.Data())){
      book<TH1F>(name+"_mass",    ";mass_{"+name+"}; Events / bin",       50,      70,     170.0);
      book<TH1F>(name+"_mass_ext",";mass_{"+name+"}; Events / bin",      100,     170,    1170.0);
      book<TH1F>(name+"_mass_inc",";mass_{"+name+"}; Events / bin",      275,      70,    1170.0);
    } else {
      book<TH1F>(name+"_mass",   ";mass_{"+name+"}; Events / bin",        65,       0,     130.0);
    }
    if (FindInString("Z1",name.Data())){
      book<TH2F>("Z1vsZ2_pt",    ";p_{T,Z_1};p_{T,Z_2}",                 100,       0.,    500,   100,       0.,    500);
      book<TH2F>("Z1vsZ2_eta",   ";#eta_{Z_1};#eta_{,Z_2}",              100,      -5.0,     5.0, 100,      -5.0,     5.0);
      book<TH2F>("Z1vsZ2_phi",   ";#phi_{Z_1};#phi_{,Z_2}",              100,      -4.0,     4.0, 100,      -4.0,     4.0);
      book<TH2F>("Z1vsZ2_mass",  ";mass_{Z_1};mass_{,Z_2}",               65,       0,     130.0,  65,       0,     130.0);
    }
  }
  book<TH1F>("AlternativeZ_mass", ";mass_{Z}; Events / bin",              65,       0,     130.0);
  book<TH1F>("AllZ_mass",         ";mass_{Z}; Events / bin",              65,       0,     130.0);

  max_index = 5;
  for (const TString& lep: {"ele", "muo", "lep"}){
    TString name;
    for(int i=1; i<=max_index; i++){
      name = lep+to_string(i);
      book<TH1F>(name+"_pt",       ";p_{T, "+name+"}; Events / bin",     100,       0.,    500/i);
      book<TH1F>(name+"_eta",      ";#eta_{"+name+"}; Events / bin",     100,      -5.0,     5.0);
      book<TH1F>(name+"_phi",      ";#phi_{"+name+"}; Events / bin",     100,      -4.0,     4.0);
    }
    name = lep+"1vs"+lep+"2";
    book<TH2F>(name+"_pt",          ";p_{T,"+lep+"1};p_{T,"+lep+"2}",    50,       0.,   1000,     50,       0.,  1000);
    book<TH2F>(name+"_eta",         ";#eta_{"+lep+"1};#eta_{"+lep+"2}",  100,      -5.0,     5.0,  100,      -5.0,    5.0);
    book<TH2F>(name+"_eta_abs",     ";#eta_{"+lep+"1};#eta_{"+lep+"2}",  100,      -0.0,     5.0,  100,      -0.0,    5.0);
  }
  book<TH1F>("cross_cleaning", ";#Delta R;Events",100,0,0.5);
  book<TH1F>("check_smart_cut",";InvMassll;Events",100,0,100);
  book<TH1F>("leptons_combinations",";InvMass_All_ll;Events",100,0,100);
  for(int i=0;i<2;++i){
    TString label = to_string(i+1);
    book<TH2F>("HvsZ"+label+"_pt",    ";p_{T,H};p_{T,Z_2}",                 100,       0.,    500,   100,       0.,    500);
    book<TH2F>("HvsZ"+label+"_eta",   ";#eta_{H};#eta_{,Z_2}",              100,      -5.0,     5.0, 100,      -5.0,     5.0);
    book<TH2F>("HvsZ"+label+"_phi",   ";#phi_{H};#phi_{,Z_2}",              100,      -4.0,     4.0, 100,      -4.0,     4.0);
    book<TH2F>("HvsZ"+label+"_mass",  ";mass_{H};mass_{,Z_2}",               65,       60,     200.0,  65,       0,     130.0);
  }
  for(int i=0;i<4;++i){
    TString label = to_string(i+1);
    book<TH2F>("H_MvsLep"+label+"_pt",    ";m_{H};p_{T,lep}",                 100,       0.,    500,   100,       0.,    500);
  }
  book<TH1F>("DNN_score", ";DNN score;Events / bin", 100,0.0,1.0);
  book<TH1F>("dZ", ";dz;Events / bin",100,-1.0,1.0);
  book<TH1F>("deltaZ", ";#Delta Z;Events / bin",100,0.0,2.0);
}

void HiggsFourLeptonsHists::fill(const HiggsFourLeptonsEvent & event){
  double weight = event.weight;
  hist<TH1F>("sumweights")->Fill(1, weight);

  std::string label = event.eventCategory();
  if (label=="undefined") label = "undef.";
  if (label=="multiple") label = ">4l";
  hist<TH1F>("eventCategory")->Fill(label.c_str(), weight);

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
    TString name = "Z"; name += to_string((i+1));
    hist<TH1F>(name+"_pt")->Fill(boson.Pt(), weight);
    hist<TH1F>(name+"_eta")->Fill(boson.Eta(), weight);
    hist<TH1F>(name+"_phi")->Fill(boson.Phi(), weight);
    hist<TH1F>(name+"_mass")->Fill(boson.M(), weight);
    if (i==1){
      TLorentzVector boson1 = (*event.reco_Z_bosons).at(0);
      hist<TH2F>("Z1vsZ2_pt")->Fill(boson1.Pt(), boson.Pt(), weight);
      hist<TH2F>("Z1vsZ2_eta")->Fill(boson1.Eta(), boson.Eta(), weight);
      hist<TH2F>("Z1vsZ2_phi")->Fill(boson1.Phi(), boson.Phi(), weight);
      hist<TH2F>("Z1vsZ2_mass")->Fill(boson1.M(), boson.M(), weight);
    }
  }

  for(int i=0; i<lep_size; i++){
    const FlavorParticle lep1 = (*event.H_leptons).at(i);
    for(int j=i+1; j<lep_size; j++){                                             
      if (j>i+4) continue;
      const FlavorParticle lep2 = (*event.H_leptons).at(j);
      TLorentzVector z1 = lep1.p4()+lep2.p4();
      hist<TH1F>("AllZ_mass")->Fill(z1.M(), weight);
      if (lep1.charge()==lep2.charge()) continue;
      hist<TH1F>("AlternativeZ_mass")->Fill(z1.M(), weight);
    }
  }

  for(int i=0; i<H_size; i++){
    TLorentzVector boson = (*event.reco_H_bosons).at(i);
    TString name = "H";
    hist<TH1F>(name+"_pt")->Fill(boson.Pt(), weight);
    hist<TH1F>(name+"_eta")->Fill(boson.Eta(), weight);
    hist<TH1F>(name+"_phi")->Fill(boson.Phi(), weight);
    hist<TH1F>(name+"_mass")->Fill(boson.M(), weight);
    hist<TH1F>(name+"_mass_ext")->Fill(boson.M(), weight);
    hist<TH1F>(name+"_mass_inc")->Fill(boson.M(), weight);

  }

  for(int i=0; i<ele_size; i++){
    TString postfix = (i>=max_index)? to_string(max_index) : to_string(i+1);
    const Electron ele = (*event.H_electrons).at(i);
    hist<TH1F>("ele"+postfix+"_pt")->Fill(ele.pt(), weight);
    hist<TH1F>("ele"+postfix+"_eta")->Fill(ele.eta(), weight);
    hist<TH1F>("ele"+postfix+"_phi")->Fill(ele.phi(), weight);

     hist<TH1F>("dZ")->Fill(ele.dz(),weight);

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

    hist<TH1F>("dZ")->Fill(muo.dz(),weight);

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
  //cross_cleaning, -> check for DeltaR(e,mu)>0.05
  for(int i=0; i<ele_size;i++){
    const Electron el_tmp = (*event.H_electrons).at(i);
    for(int j=0; j<muo_size; j++){
      const Muon muo_tmp = (*event.H_muons).at(j);
        hist<TH1F>("cross_cleaning")->Fill(deltaR(el_tmp,muo_tmp),weight);
    }
  }
  //Check if the smart cut is working
  for(int i=0;i<lep_size; i++){
    const FlavorParticle lep1 = (*event.H_leptons).at(i);
    for(int j=i+1;j<lep_size; j++){
      const FlavorParticle lep2 = (*event.H_leptons).at(j);
      if(lep1.charge()!=lep2.charge()){
        TLorentzVector pair = lep1.p4() + lep2.p4();
        hist<TH1F>("check_smart_cut")->Fill(pair.M(),weight);
        hist<TH1F>("deltaZ")->Fill(fabs(lep1.p4().Pz()-lep2.p4().Pz()),weight);
        


      }
    }   
  }
  //invariant mass, all leptons combinations, no flavor nor charge considerations
  for(int i=0;i<lep_size; i++){
    const FlavorParticle lep1 = (*event.H_leptons).at(i);
    for(int j=i+1;j<lep_size; j++){
      const FlavorParticle lep2 = (*event.H_leptons).at(j);
        TLorentzVector pair = lep1.p4() + lep2.p4();
        hist<TH1F>("leptons_combinations")->Fill(pair.M(),weight);
    }
  }
  //Correlations Higgs with the two Z bosons
  for(int i=0;i<H_size;i++){
    TLorentzVector bosonH = (*event.reco_H_bosons).at(i);
    for(int j=0;j<4;++j){
      TLorentzVector lep = (*event.H_leptons).at(j+4*i).p4();
      TString label = to_string(j+1);
       hist<TH2F>("H_MvsLep"+label+"_pt")->Fill(bosonH.M(),lep.Pt(),weight);
    }
    for(int j=0;j<2*H_size;j++){
      TLorentzVector bosonZ = (*event.reco_Z_bosons).at(j);
      TString index = to_string(j+1);
      hist<TH2F>("HvsZ" + index +"_pt")->Fill(bosonH.Pt(),bosonZ.Pt(),weight);
      hist<TH2F>("HvsZ" + index +"_eta")->Fill(bosonH.Eta(),bosonZ.Eta(),weight);
      hist<TH2F>("HvsZ" + index +"_phi")->Fill(bosonH.Phi(),bosonZ.Phi(),weight);
      hist<TH2F>("HvsZ" + index +"_mass")->Fill(bosonH.M(),bosonZ.M(),weight);
    }
  }
  hist<TH1F>("DNN_score")->Fill(event.dnn_output(),weight);
}