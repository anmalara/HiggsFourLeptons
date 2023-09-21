from tdrstyle_all import * #LEAF/Generator/tdrstyle_all.py

import os 
import ROOT
import numpy as np
from ModuleRunnerBase import GenericPath

def main():
    generic = GenericPath()
    # years = ['UL16postVFP','UL16preVFP','UL17','UL18']
    years = ['UL16preVFP','UL18']
    names = ['Data','VV','ggH','VBF']
    path = generic.pnfs_path + '/Analyses/HiggsFourLeptons/'
    #regions = ['nominal','H_m_reco','Z_m_reco','H_m_geq_180']

    rebin = 5
    colors_years = {'UL16preVFP' : ROOT.kBlue, 'UL16postVFP' : ROOT.kRed, 'UL17' : ROOT.kOrange, 'UL18' : ROOT.kBlack}
    hist = {}
    canvas = {}
    legends = {}

    for year in years:
        for name in names:
            fname = path + year + '/HiggsFourLeptons/' + 'DATA__' + name + '_standard_' + year + '.root'
            if(not 'Data' in name):
                fname = fname.replace('DATA','MC')
            f = ROOT.TFile(fname)
            hist[year+name] = f.Get('nominal_H4l/DNN_score')
            hist[year+name].Rebin(rebin)
            #f.cd()
            if(hist[year+name].Integral()!=0):
                hist[year+name].Scale(1.0/hist[year+name].Integral())
            hist[year+name].SetDirectory(0)
    for name in names:
        canvas[name] = tdrDiCanvas('can_' + name, 0.0, 1.0, 0.0, 0.2, 0.0, 2.0, 'DNN_score', 'Arbitrary units', 'Ratio')
        legends[name] = tdrLeg(0.7, 0.7, 0.9, 0.9,textSize=0.03)
        for year in years:
            legends[name].AddEntry(hist[year+name],year,'P')
    for name in names:
        for year in years:
                hist[year+name] = hist[year+name].Clone(year+name)
                canvas[name].cd(1)
                tdrDraw(hist[year+name], 'P', mcolor= colors_years[year], fstyle=0)#,fcolor=colors_reg[region]

        canvas[name].SaveAs(generic.analysis_path +'/PostAnalyzer/pdfs/Yearcomparison/' + 'CombinedYears_' + name + '.pdf')

if __name__ == '__main__':
	main()
