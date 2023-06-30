import cgi
import ROOT
import sys
import os
from ModuleRunnerBase import GenericPath

ROOT.gROOT.SetBatch(1)

def DrawHist(path,samples,histname,save_loc,save_name,opt):
    c = ROOT.TCanvas("c","MyCanvas",800,600)
    vbf = samples[0]
    rootfile = 'MC__' + vbf + '_standard_UL18.root'
    f_vbf = ROOT.TFile(path + rootfile)
    h_vbf = ROOT.TH1F(f_vbf.Get('nominal_H4l/'+histname))
    h_vbf.SetStats(0)
    h_vbf.SetLineColor(ROOT.kBlue)
    h_vbf.Scale(1.0/h_vbf.Integral())
    h_vbf.Draw()
    ggh = samples[1]
    rootfile = 'MC__' + ggh + '_standard_UL18.root'
    f_ggh = ROOT.TFile(path + rootfile)
    h_ggh = ROOT.TH1F(f_ggh.Get('nominal_H4l/'+histname))
    h_ggh.SetStats(0)
    h_ggh.Scale(1.0/h_ggh.Integral())
    h_vbf.SetLineColor(ROOT.kRed)
    h_ggh.Draw('same hist')

    legend = ROOT.TLegend(0.1,0.7,0.3,0.9)
    legend.SetHeader('Samples','C')
    legend.AddEntry(h_vbf,'VBF' ,'l')
    legend.AddEntry(h_ggh,'ggH' ,'l')
    legend.Draw()

    c.SaveAs(save_loc + '/' + save_name)


def main():
    generic = GenericPath()
    year = 'UL18'
    samples = ['VBF','ggH']
    histname = 'DNN_score'
    path = generic.pnfs_path + '/Analyses/HiggsFourLeptons/UL18/HiggsFourLeptons/'
    options = 'same'
    save_location_path = generic.analysis_path + '/PostAnalyzer/pdfs'

    path_ = os.path.join(save_location_path + '/' + 'DNN')
    if(not os.path.isdir(path_)):
        os.mkdir(path_)
    save_name = 'DNN_score_bck.pdf'

    DrawHist(path,samples,histname,path_,save_name,options)


if __name__ == '__main__':
    main()
