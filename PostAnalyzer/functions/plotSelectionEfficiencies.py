import os 
import ROOT
import sys
import numpy as np
from ModuleRunnerBase import GenericPath


def main():
    generic = GenericPath()

    step_efficiencies = ['weights','triggers','nominal']
    BinNumber = len(step_efficiencies)
    years = ['UL18']
    types = ['MC','DATA']
    families = ['ggH','VBF','VV', 'DY', 'Data']
    path_root = generic.pnfs_path + '/Analyses/HiggsFourLeptons/UL18/HiggsFourLeptons/'
    save_loc = generic.analysis_path +'/PostAnalyzer/pdfs'
    save_name = 'selectionEfficiencies'
    histograms = []
    histograms_relative = []
    efficiencies_mat = []
    names = []

    for year in years:
        for type in types:
            for family in families:
                rootfile = type + '__' + family + '_standard_' + year + '.root' 
                path = path_root+'/'+rootfile
                if(not os.path.isfile(path)): 
                    continue
                eff = []
                for step in step_efficiencies:
                    histname = step + '_H4l/' + 'sumweights'
                    eff.append(extractTotalWeightFromHist(path,histname))
                efficiencies_mat.append(eff)
                name = family + step
                histograms.append(createHistogram(eff,step_efficiencies,BinNumber,name,False))
                histograms_relative.append(createHistogram(eff,step_efficiencies,BinNumber,name,True))
                names.append(family)
    mergeHistograms(histograms,names,save_loc,save_name,False)
    mergeHistograms(histograms_relative,names,save_loc,save_name+'_relative',True)

def extractTotalWeightFromHist(filename,histname):
    '''
        Extract total number of entries in a histogram family.
        Given that the first histogram is the one containing the weight.
    '''
    f = ROOT.TFile(filename)
    h2 = f.Get(histname)
    count = h2.GetBinContent(1)
    f.Close()
    return count

def createHistogram(efficiencies,xlabels,BinNumber,name,relative):
    h = ROOT.TH1D( name, ';; Selection efficiency', BinNumber, 0., 1.)
    normalization = max(efficiencies)
    xaxis = h.GetXaxis()
    h.GetYaxis().SetRangeUser(1e-03, 10.0)
    for i in range(len(efficiencies)):
        if(not relative):
            print('Value of sample ',name,' at step ',xlabels[i], ' ',efficiencies[i])
        try:
            if(not relative):
                content = efficiencies[i]/normalization
            else:
                if(i==0):
                    content = efficiencies[i]/normalization
                else:
                    content = efficiencies[i]/efficiencies[i-1]
        except ZeroDivisionError:
            print('Entry value of file is zero')
        h.SetBinContent (i+1, content)
        xaxis.SetBinLabel(i+1,xlabels[i])
    h.SetStats(0)
    return h

def mergeHistograms(ar_hists,names,save_loc,save_name,relative):
    c = ROOT.TCanvas()
    c.SetLogy(1)
    colors = [40,41,46,38,30,28,11]
    legend = ROOT.TLegend(0.7,0.7,0.9,0.9)
    legend.SetHeader('Samples','C')

    for i in range(len(ar_hists)):
        ar_hists[i].SetFillStyle(0)
        ar_hists[i].SetLineWidth(3)
        ar_hists[i].SetLineColor(colors[i])
        ar_hists[i].GetXaxis().SetTickSize(0.0)
        ar_hists[i].Draw('same')
        legend.AddEntry(ar_hists[i],names[i] ,'l')
    legend.SetNColumns(2)
    legend.Draw()
    

    c.SetGridy(1)
    c.SaveAs(save_loc + '/' +save_name + '.pdf')


if __name__ == '__main__':
	main()
