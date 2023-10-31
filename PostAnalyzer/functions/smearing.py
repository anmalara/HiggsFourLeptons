import ROOT
import sys
import os
import numpy as np
from ModuleRunnerBase import GenericPath
from ModuleRunnerBase import VariablesBase
from tdrstyle_all import *

ROOT.gROOT.SetBatch(1)

class Smearer(VariablesBase):
    def __init__(self):
        VariablesBase.__init__(self)
        generic = GenericPath()
        self.year = 'UL18'
        self.extension = 'standard'
        self.sample = 'MC__DYJetsToLL_M-50'
        self.file_path = '/pnfs/iihe/cms/store/user/bhonore/Analyses/HiggsFourLeptons/'+ self.year +'/HiggsFourLeptons/'
        self.path = self.file_path + self.sample + '_' + self.extension + '_' + self.year + '.root'
        self.histname = 'H_mass'
        self.save_loc = generic.analysis_path +'/PostAnalyzer/pdfs/Smearing/'
        self.save_name = 'smeared_' + self.sample + '_' + self.histname + '.pdf'

    def smearing(self,iter=1):
        c = tdrDiCanvas('SmearingCanvas', 70.0, 170.0, 0.0, 30.0, 0.0, 2.0, 'Smearing', 'Arbitrary units', 'Ratio')
        tfile = ROOT.TFile(self.path)
        hist = tfile.Get('nominal_H4l/'+self.histname)
        # print(self.path)
        new_hist = ROOT.TH1F('Smeared_'+self.histname,'Title',hist.GetNbinsX(),hist.GetXaxis().GetXmin(),hist.GetXaxis().GetXmax())
        c.cd(1)
        binshift = 70
        hist_ = ROOT.TH1F('Smeared_tmp'+self.histname,'Title_',hist.GetNbinsX(),hist.GetXaxis().GetXmin(),hist.GetXaxis().GetXmax())
        hist_ = hist.Clone('work_hist')
        for it in range(iter):
            negative_entries = 0
            if(it>0):
                hist_ = new_hist.Clone('work_hist')#copy current iteration
                new_hist *= 0 #reset for next iteration
            for i in range(hist_.GetNbinsX()):
                print('Bin Number :',i)
                if(hist_.GetBinContent(i)<=0):
                    negative_entries += 1
                else:
                    binwidth = hist_.GetXaxis().GetBinWidth(i)
                    # print('--> Bin width : ',hist_.GetXaxis().GetBinWidth(i))
                    print('--> Bin content : ',hist_.GetBinContent(i))
                    genNumber = np.random.normal(hist_.GetBinContent(i),np.sqrt(3*binwidth),1)
                    # print('--> Gen content : ',genNumber)
                    new_hist.Fill(binshift+i*binwidth,genNumber[0])
            print('negative entries : ',negative_entries)
            # print(new_hist.Integral())
            # print(hist.Integral()-new_hist.Integral())

        #Set poissonian errors
        for i in range(hist.GetNbinsX()):
            if(new_hist.GetBinContent(i)>0):
                new_hist.SetBinError(i,np.sqrt(new_hist.GetBinContent(i)))
        ratio_hist = ROOT.TH1F('Smeared_ratio_'+self.histname,'Title_ratio',hist.GetNbinsX(),hist.GetXaxis().GetXmin(),hist.GetXaxis().GetXmax())
        ratio_hist = new_hist.Clone('cloned_hist')
        ratio_hist.Divide(hist)

        #hist.SetDirectory(0)
        c.cd(1)
        legend = tdrLeg(0.6, 0.7, 0.9, 0.9,textSize=0.03)
        legend.AddEntry(hist,'MC__DYJetsToLL_M-50'+self.histname,'P')
        legend.AddEntry(new_hist,'Smearing','P')
        tdrDraw(hist, 'P', mcolor= ROOT.kBlue, fstyle=0)#,fcolor=colors[name]
        c.cd(1)
        tdrDraw(new_hist, 'P', mcolor= ROOT.kRed, fstyle=0)#,fcolor=colors[name]
        c.cd(2)
        tdrDraw(ratio_hist, 'P', mcolor= ROOT.kBlack, fstyle=0)#,fcolor=colors[name]
        c.SaveAs(self.save_loc +self.save_name)
        tfile.Close()

def main():
    Smearer().smearing(iter=1)
if __name__ == '__main__':
	main()
        

#Previous code
# genEntries = np.random.normal(0,0.5*3*binwidth, int(hist_.GetBinContent(i)))
# genEntries_int = [int(x) for x in genEntries]
# weight = hist_.GetBinContent(i)/len(genEntries)
# print(genEntries_int)
# if(len(genEntries_int)>0):
#     for j in range(min(genEntries_int),max(genEntries_int)+1):
#         if((0<=(i+j))and((i+j)<=hist_.GetNbinsX())):
#             new_hist.Fill(binshift+(i+j)*binwidth,weight*genEntries_int.count(j))