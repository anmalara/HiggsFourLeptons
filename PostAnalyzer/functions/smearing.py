#! /usr/bin/env python
import ROOT as rt
import numpy as np
from collections import OrderedDict
from ModuleRunnerBase import GenericPath
from ModuleRunnerBase import VariablesBase
from tdrstyle_all import *
from printing_utils import green, blue, prettydict
import os

rt.gROOT.SetBatch(1)

class Smearer(VariablesBase):
    def __init__(self,year,simudata,sample,histname,type,region,rebin=1,rootfileSaveLoc='',nameext=''):
        VariablesBase.__init__(self)
        generic = GenericPath()
        self.year = year #'UL18'
        self.extension = 'standard'
        self.sample = simudata+'__'+sample#'MC__DYJetsToLL_M-50'
        self.type = type#'DY'
        self.region = region#'nominal'
        self.rebin = rebin
        self.file_path = '/pnfs/iihe/cms/store/user/bhonore/Analyses/HiggsFourLeptons/'+ self.year +'/HiggsFourLeptons/'
        self.path = self.file_path + self.sample + '_' + self.extension + '_' + self.year + '.root'
        self.histname = histname
        self.save_loc_pdf = generic.analysis_path +'/PostAnalyzer/pdfs/Smearing/'
        if(rootfileSaveLoc==''):
            self.save_loc_root = generic.analysis_path + '/PostAnalyzer/pdfs/Smearing/'
        elif(rootfileSaveLoc=='datacards'):
            self.save_loc_root = generic.analysis_path + '/PostAnalyzer/datacards/rootfiles_for_datacards/' + self.year + '/' + self.region
        else:
            self.save_loc_root = rootfileSaveLoc
        if(nameext==''):
            self.save_name = 'histograms-' + self.histname + '-' + self.region + '-' + self.type + '-' + self.year 
        else:
            self.save_name = 'histograms-' + self.histname + '-' + self.region + '-' + self.type + '-' + self.year + '-' + nameext

    def smearing(self,process=False,iter=1):
        #staterror = True -> Shape smearing
        #staterror = False -> Only add statistical uncertainty
        if(not os.path.exists(self.path)):
            print('The file at ',self.path,' does not exist')
        tfile = rt.TFile(self.path)
        hist = tfile.Get(self.region+'_H4l/'+self.histname)
        hist.SetDirectory(0)
        tfile.Close()
        smeared_hists = OrderedDict([(0, hist.Clone('smear_0'))])
        nbins = 2
        for it in range(1,iter+1):
            np.random.seed(10)
            old_hist = smeared_hists[it-1]
            new_hist = old_hist.Clone('smear_'+self.type+'_'+str(it))
            new_hist.SetDirectory(0)
            for bin in range(old_hist.GetNbinsX()+1):
                width = old_hist.GetBinWidth(bin)
                if(process):
                    content = old_hist.GetBinContent(bin)  
                    if content<=0:
                        bin_content = 0
                    else:
                        bin_content = np.random.normal(content,np.sqrt(old_hist.GetBinContent(bin)))
                else:
                    # #Neglect boundary bins
                    # if (bin+nbins>old_hist.GetNbinsX()):
                    #    bin_content=old_hist.GetBinContent(bin)#/(bin+nbins-old_hist.GetNbinsX()+1)
                    # elif (bin-nbins<0):
                    #     bin_content=old_hist.GetBinContent(bin)#/(nbins-bin+1)
                    #else:
                        norma = min(bin+nbins,old_hist.GetNbinsX()+1)-max(bin-nbins,0)+1
                        mean = old_hist.Integral(max(bin-nbins,0),min(bin+nbins,old_hist.GetNbinsX()+1))
                    # if(bin-nbins)<0:
                    #     mean += old_hist.Integral(old_hist.GetNbinsX()+bin-nbins,old_hist.GetNbinsX())/norma
                    # if((bin+nbins)>old_hist.GetNbinsX()):
                    #     mean += old_hist.Integral(0,bin+nbins-old_hist.GetNbinsX())/norma
                        bin_content = np.random.normal(mean,np.sqrt(nbins*width))
                    
                new_hist.SetBinContent(bin,bin_content)
            new_hist.Scale(hist.Integral()/new_hist.Integral())
            for bin in range(new_hist.GetNbinsX()+1):
                bin_content = new_hist.GetBinContent(bin)
                err = np.sqrt(bin_content) if bin_content>0 else 0
                new_hist.SetBinError(bin,err)
            smeared_hists[it] = new_hist
            if(process):
                #Put the only hist at the end
                smeared_hists[iter] = new_hist
                break

        smearprocess = 'Shape'
        if(process):
            smearprocess = 'Staterror'

        File = rt.TFile(self.save_loc_root + '/' +self.save_name+'_'+smearprocess+'.root','RECREATE')
        File.cd()
        
        smeared_hists[iter].Rebin(self.rebin)
        smeared_hists[iter].Write(self.histname + '_' + self.region + '_' + self.type + '_' + self.year + '_' + 'IsSmeared_' + smearprocess)
        print(green('Smeared histogram written at {}'.format(self.save_loc_root + '/' +self.save_name+'_'+smearprocess+'.root')))
        File.Close()    

        ratio_hists = {}
        yaxismax = max(smeared_hists[iter].GetMaximum(),hist.GetMaximum())
        if(self.histname=='H_mass'):
            xmin = 70.0
        else:
            xmin = 0.0
        #If shape smaering, store the evolution of the smearing
        if(not process):
            c = tdrDiCanvas('SmearingCanvas_'+ self.region + self.type +str(iter)+'_'+smearprocess, xmin, 170.0, 0.0,yaxismax + np.sqrt(yaxismax) , 0.0, 2.0, 'Smearing', 'Arbitrary units', 'Ratio')
            c.cd(1)
            legend = tdrLeg(0.6, 0.7, 0.9, 0.9,textSize=0.03)
            tdrDraw(hist, 'P', mcolor= rt.kAzure+2, fstyle=0)
            legend.AddEntry(hist,'MC__DYJetsToLL_M-50'+self.histname,'P')
            for ind in range(max(1,iter-1),iter+1):
                c.cd(1)
                hist_ = smeared_hists[ind]
                col = rt.kGreen+2 if iter==ind else rt.kRed+1
                tdrDraw(hist_, 'P', mcolor= col, fstyle=0)
                legend.AddEntry(hist_,'Smearing '+str(ind),'P')
                ratio_hists[ind] = hist_.Clone('ratio_'+str(ind))
                # ratio_hists[ind].Divide(hist)
                c.cd(2)
                tdrDraw(ratio_hists[ind], 'P', mcolor= col, fstyle=0)
            c.SaveAs(self.save_loc_pdf +self.save_name+"_"+str(iter)+ '_' + smearprocess + '.pdf')

# def main():
#     smearer = Smearer('UL18','MC','DYJetsToLL_M-50','DY','nominal','datacards')
#     # smearer.smearing(iter=0)
#     smearer.smearing(iter=100)
#     smearer2 = Smearer('UL18','MC','ggH','ggH','H_m_reco','datacards')
#     smearer2.smearing(iter=50)

#     smearer3 = Smearer('UL18','DATA','Data','Data','nominal','datacards')
#     smearer3.smearing(iter=50)
#     # smearer.smearing(iter=2)
#     # smearer.smearing(iter=5)
#     # smearer.smearing(iter=10)
#     # smearer.smearing(iter=20)
#     # smearer.smearing(iter=50)
#     # smearer.smearing(iter=100)
    

# if __name__ == '__main__':
#     main()