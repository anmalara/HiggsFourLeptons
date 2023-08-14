import os 
import ROOT
import numpy as np
from ModuleRunnerBase import GenericPath


def main():
    generic = GenericPath()

    years = ['UL18']
    types = ['MC','DATA']
    samples = ['ggH','VBF','VV','Data']#,'DY'
    #samples = ['VV','Data']#,'DY'
    normalizer = ''
    histograms = ['ele_iso_rel_03_lowPtLep','ele_iso_rel_03_charged_lowPtLep','muo_iso_rel_04_lowPtLep','muo_iso_rel_03_lowPtLep','muo_iso_rel_03_charged_lowPtLep','muo_iso_tk_lowPtLep']
    families = ['nominal','H_m_reco','Z_m_reco','H_m_geq_180','4e','4m','2m2e']
    path_root_ = generic.pnfs_path + '/Analyses/HiggsFourLeptons/'
    save_loc_ = generic.analysis_path +'/PostAnalyzer/pdfs/Isolation'
    save_loc = ''
    histograms_info = []
    names = []

    for hist in histograms:
        save_loc = save_loc_ + '/' + hist
        histograms_info = []
        for year in years:
            path_root = path_root_ + year + '/HiggsFourLeptons'
            for family in families:
                histograms_info.append([])
                for type_ in types:
                    for sample in samples:
                        rootfile = type_ + '__' + sample + '_standard_' + year + '.root' 
                        path = path_root+'/'+rootfile
                        normalizer_path = path_root + '/' + type_ + '__' + sample + '_standard_' + year + '.root'
                        if(not os.path.isfile(path)): 
                            continue
                        if(not os.path.isfile(normalizer_path)):
                            continue
                        histname = family + '_H4l/' + hist
                        normalizer_histname = normalizer + '_H4l/' + hist
                        histograms_info[-1].append([path,histname,sample,hist + '_' +family,normalizer_path,normalizer_histname])
                        names.append(sample)
        for elem in histograms_info:#for each sample
            if(len(elem)>0):
                mergeHistograms(elem,names,save_loc,normalizer)

def mergeHistograms(ar_hists,names,save_loc,normalizer):
    save_name = ar_hists[0][3]
    c = ROOT.TCanvas('c','c',800,600)
    colors = [40,41,46,38,30,28,11]
    legend = ROOT.TLegend(0.7,0.7,0.9,0.9)
    legend.SetHeader('Samples','C')
    rebinning = 5
    
    if(normalizer != ''):
        g = ROOT.TFile(ar_hists[0][4])
        normalizer_hist = g.Get(ar_hists[0][5]).Clone('ar_hists05')
        normalizer_hist.Rebin(rebinning)
        if(normalizer_hist.Integral() != 0):             
            normalizer_hist.Scale(1.0/normalizer_hist.Integral())
    hist_list = []
    for i in range(len(ar_hists)):
        f = ROOT.TFile(ar_hists[i][0])
        histo = f.Get(ar_hists[i][1])
        hist_list.append(histo)
        histo.SetDirectory(0)
        f.Close()
        histo.SetStats(0)
        histo.Rebin(rebinning)
        if(histo.Integral() != 0):             
            histo.Scale(1.0/histo.Integral())
        if(normalizer != ''):
            histo.Divide(normalizer_hist)
        #histo.GetYaxis().SetRangeUser(0.0, )#maximum+0.005
        histo.SetLineWidth(3)
        histo.SetLineColor(colors[i])
        if i==0:
            histo.Draw()
        else:
            histo.Draw('same')
        legend.AddEntry(histo,names[i] ,'l')
    legend.SetNColumns(2)
    legend.Draw()

    c.SetGridy(1)
    if(normalizer==''):
        c.SaveAs(save_loc + '/' + save_name + '' + '.pdf')
    else:
        c.SaveAs(save_loc + '/' + save_name + '_normalized.pdf')
    
    c.Close()

if __name__ == '__main__':
	main()
