from tdrstyle_all import * #LEAF/Generator/tdrstyle_all.py

import os 
import ROOT
import numpy as np
from ModuleRunnerBase import GenericPath
from printing_utils import green, blue, prettydict
import smearing

def createCombineRootFiles(year,name,region,histogram,rmNegBin,rebin=1):
    generic = GenericPath()
    path = generic.pnfs_path + '/Analyses/HiggsFourLeptons/'
    rootfile_path = '/ada_mnt/ada/user/bhonore/WorkingArea/CMSSW_10_6_28/src/LEAF/HiggsFourLeptons/PostAnalyzer/datacards/rootfiles_for_datacards'
    hist = {}

    if((region=='H_m_geq_180')and(histogram=='H_mass')):
        histogram = 'H_mass_ext'

    savepath = rootfile_path + '/' + year + '/' + region + '/histograms-'+histogram + '-' + region + '-' + name + '-' + year + '-NotSmeared' + '.root'
    fname = path + year + '/HiggsFourLeptons/' + 'DATA__' + name + '_standard_' + year + '.root'
    if(not 'Data' in name):
        fname = fname.replace('DATA','MC')

    File = ROOT.TFile(savepath,'RECREATE')
    if(os.path.exists(fname)):
        f = ROOT.TFile(fname)
    hist[year+region+name] = f.Get(region + '_H4l/'+histogram)
    hist[year+region+name].Rebin(rebin)
    hist_temp = f.Get(region + '_H4l/'+histogram)
    #set negative entries to zero
    if(rmNegBin):
        for bin in range(hist[year+region+name].GetNbinsX()):
                if hist[year+region+name].GetBinContent(bin)<0:
                    hist[year+region+name].SetBinContent(bin, hist[year+region+name].GetBinContent(bin))
    #remove empty bins in signal region
    if(region=='H_m_reco')and(histogram=='H_mass'):
        print('REMOVING SOME BINS')
        hist[year+region+name] = ROOT.TH1F("name", "", 5, 120, 130)
        newbin =0
        for bin in range(hist_temp.GetNbinsX()):
            if hist_temp.GetBinContent(bin)==0 and hist_temp.GetBinError(bin)==0: continue
            newbin += 1
            hist[year+region+name].SetBinContent(newbin, hist_temp.GetBinContent(bin))
    File.cd()
    #Write in the histograms folder
    hist[year+region+name].Write(histogram + '_' + region + '_' + name + '_' + year + '_NotSmeared')

    print(green('---> \t Rootfile created at {} '.format(savepath)))
    File.Close()

def CreateFakeData(year,signals,region,histogram,rebin=1,smearing_iter=300):
    generic = GenericPath()
    #real data will only be used to normalize fake data to real data
    datapath = generic.pnfs_path + '/Analyses/HiggsFourLeptons/' + year + '/HiggsFourLeptons/' + 'DATA__Data_standard_' + year + '.root'
    rootfile_path = '/ada_mnt/ada/user/bhonore/WorkingArea/CMSSW_10_6_28/src/LEAF/HiggsFourLeptons/PostAnalyzer/datacards/rootfiles_for_datacards'
    hist = {}
    if((region=='H_m_geq_180')and(histogram=='H_mass')):
        histogram = 'H_mass_ext'
    savepath = rootfile_path + '/' + year + '/' + region + '/histograms-'+histogram + '-' + region + '-' + 'Data' + '-' + year + '-IsSmeared_Staterror'+'.root'
    #Add smearing MC files to create a fake data
    for i in range(len(signals)):
        type = 'MC'
        try:
            if('Data' in signals[i]):
                raise TypeError('Cant display real datafile')
        except TypeError as err:
            err.add_note('ERROR, Data samples can not be used. {} is a datafile'.format(signals[i]))
               
        #Apply some smearing
        SMer = smearing.Smearer(year,type,signals[i],histogram,signals[i],region,rebin,'datacards','IsSmeared')
        SMer.smearing(True,smearing_iter)
        SMer.smearing(False,smearing_iter)

        #Creating the fake data file
        fname = rootfile_path + '/' + year + '/' + region + '/'  + 'histograms-' + histogram + '-' + region + '-' + signals[i] + '-' + year + '-IsSmeared_Staterror.root'
        #Fill the file
        if(os.path.exists(fname)):
            f = ROOT.TFile(fname)
        else:
            print('ERROR, file {} doesnt exist'.format(fname))
        if(i==0):            
            hist[year+region+signals[0]] = ROOT.TH1F(f.Get(histogram + '_' + region + '_' + signals[0] + '_' + year + '_IsSmeared_Staterror').Clone(year+region+signals[0]))
            hist[year+region+signals[0]].SetDirectory(0)
           
        else:
            hist[year+region+signals[i]] = ROOT.TH1F(f.Get(histogram + '_' + region + '_' + signals[i] + '_' + year + '_IsSmeared_Staterror').Clone(year+region+signals[i]))
            hist[year+region+signals[i]].SetDirectory(0)
            hist[year+region+signals[0]].Add(hist[year+region+signals[i]])

        f.Close()
    #Access real data file to get the normalization    
    if(os.path.exists(datapath)):
        f_data = ROOT.TFile(datapath)
    else:
        print('ERROR, file {} doesnt exist'.format(datapath))

    datahist = f_data.Get(region + '_H4l/'+histogram)
    datahist.Rebin(rebin)

    #Normalize fake data file to actual data
    # hist[year+region+signals[0]].Rebin(2)
    hist[year+region+signals[0]].Scale(datahist.Integral()/hist[year+region+signals[0]].Integral())
    
    File = ROOT.TFile(savepath,'RECREATE')
    if(os.path.exists(savepath)):
        File = ROOT.TFile(savepath,'RECREATE')
    else:
        print('ERROR, file {} doesnt exist'.format(savepath))

    #Write in the histograms folder
    hist[year+region+signals[0]].Write(histogram + '_' + region + '_' + 'Data' + '_' + year + '_' + 'IsSmeared_Staterror')
    print(green('---> \t Smeared Data created at {} '.format(savepath)))
    File.Close()