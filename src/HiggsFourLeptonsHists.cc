#include "LEAF/HiggsFourLeptons/include/HiggsFourLeptonsHists.h"
#include "LEAF/Analyzer/include/constants.h"
#include "LEAF/Analyzer/include/useful_functions.h"

using namespace std;

HiggsFourLeptonsHists::HiggsFourLeptonsHists(TString dir_) : BaseHists(dir_){

  book<TH1F>("sumweights",        ";sum of event weights; Events / bin",  1,       0.5,     1.5);

}

void HiggsFourLeptonsHists::fill(const HiggsFourLeptonsEvent & event){
  double weight = event.weight;
  hist<TH1F>("sumweights")->Fill(1, weight);
}
