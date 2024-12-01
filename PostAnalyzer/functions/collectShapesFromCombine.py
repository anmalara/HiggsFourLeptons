import os
from collections import OrderedDict
import ROOT
import numpy as np
from ModuleRunnerBase import GenericPath
from tdrstyle_all import *

class Collecter():
    def __init__(self,year,region,histogram,channels):
        self.generic = GenericPath()
        self.path_datacards = self.generic.analysis_path + '/PostAnalyzer/datacards/datacards'
        self.year = year
        self.histogram = histogram
        self.region = region
        self.channels = channels
        self.diagnostic_extension = 'fitDiagnosticsTest'
        self.histos = {}
        self.colors = {'total_background' : ROOT.kMagenta,'total_signal' : ROOT.kGreen,'total' : ROOT.kBlue, 'VV' : ROOT.kRed, 'ggH' : ROOT.kOrange, 'VBF' : ROOT.kBlack, 'DY' : ROOT.kViolet ,'data' : ROOT.kYellow,'shapes_fit_s' : ROOT.kBlue,'shapes_prefit' : ROOT.kOrange}
        self.linestyles = {'shapes_fit_s' : ROOT.kSolid,'shapes_prefit' : ROOT.kDashed}
        self.legends = {'shapes_fit_s' : 'Postfit', 'shapes_prefit' : 'Prefit'}
    
    def ConvertTGraphAsymmErrorsToTH1F(self,graph):
        #From the assumption that errors in x = binwidth
        xValues = graph.GetX()
        yValues = graph.GetY()
        yErrorsLow = graph.GetEYlow()
        yErrorsHigh = graph.GetEYhigh()
        xErrorsLow = graph.GetEXlow()

        # Get the range of x-axis
        xMin = min(xValues)
        xMax = max(xValues)
        nBins = len(xValues)

        # Create a new TH1F histogram
        th1fHist = ROOT.TH1F("th1fHist", "TH1F Histogram", nBins, xMin, xMax)

        # Fill the TH1F histogram with the contents of the TGraphAsymmErrors
        for i in range(nBins):
            binContent = yValues[i]
            binErrorLow = yErrorsLow[i]
            binErrorHigh = yErrorsHigh[i]
            binError = (binErrorLow + binErrorHigh) / 2.0  # Using average of asymmetric errors for simplicity
            th1fHist.SetBinContent(i, binContent)
            th1fHist.SetBinError(i, binError)

        return th1fHist
    
    def extractData(self,plot,channel):
        #For extracting the whole output histogram
        fname = self.path_datacards + '/' + self.year + '/' + self.region + '/' + self.diagnostic_extension + '_' + self.histogram + '_' + self.region + '_' + self.year + '.root'
        #print(fname)
        if os.path.exists(fname):
            f = ROOT.TFile(fname)
            histname = plot + '/' + self.region + '/' + channel
            #print(histname)
            print(f.Get(histname))
            if(not(channel=='data')):
                self.histos[plot+channel] = f.Get(histname).Clone()
            else:
                self.histos[plot+channel] = self.ConvertTGraphAsymmErrorsToTH1F(f.Get(histname))
            #print(self.histos[plot+channel])
            
            #data histo format is TGraphAsymmErrors from combine, so rather retrieve the input file
            self.histos[plot+channel].SetDirectory(0)
            return 1
        else:
            print('ERROR : ',fname,' doesnt exist')
            return 0
    def extractBinFromData(self,channel,bin=-1):
        #For extracting one bin from the whole histogram
        fname = self.path_datacards + '/' + self.year + '/' + self.region + '/' + self.diagnostic_extension + '_' + self.histogram + '_' + self.region + '_' + self.year + '.root'
        if os.path.exists(fname):
            f = ROOT.TFile(fname)
            histname = '/shapes_prefit/ch1/' + channel
            hist = f.Get(histname)
            if(bin==-1):
                return hist.Integral()
            elif(bin>=0):
                return hist.GetBinContent(bin)
            else:
                print('Bin Number not valid')
                return 0
        else:
            print('ERROR : ',fname,' doesnt exist')
            return 0
    def plotData(self,plot,shape=False,bin=-1):
        c = ROOT.TCanvas()
        h = {}
        legend = ROOT.TLegend(0.7,0.7,0.9,0.9)
        legend.SetHeader('Samples','C')
        globalmax = 0.0
        if(shape==False):
            for j in self.channels:
                val = self.extractBinFromData(j,bin)
                if(val>globalmax):
                    globalmax = val
        if(shape==True):
            for j in self.channels:
                if(self.extractData(plot,j)):
                    hist = self.histos[plot+j].Clone()
                    val = hist.GetMaximum()
                if(val>globalmax):
                    globalmax = val
        for i in self.channels:
            h[i] = ROOT.TH1D('name' + i, ';; PreFitValue', 1, 0., 1.)
            if(shape==True):        
                h[i] = self.histos[plot+i]
            else:
                h[i].SetBinContent(1,self.extractData(i),bin)
            h[i].SetStats(0)
            h[i].GetYaxis().SetRangeUser(0, globalmax + np.sqrt(globalmax))
            h[i].SetLineColor(self.colors[i])
            h[i].SetFillStyle(0)
            h[i].SetLineWidth(3)
            h[i].GetXaxis().SetTickSize(0.0)
            h[i].SetMarkerStyle(15)
            h[i].GetYaxis().SetTitle('Events / bin')
            h[i].SetTitle(self.histogram)
            binmax = self.histos[plot+i].GetXaxis().GetXmax()
            binmin = self.histos[plot+i].GetXaxis().GetXmin()
            if(self.histogram=='DNN_score'):
                #Then x axis range is normalized
                for j in range(1,h[i].GetNbinsX()+1):
                    binlabel = float(j)/(h[i].GetNbinsX())
                    if(j%4==0):
                        h[i].GetXaxis().SetBinLabel(j, str(binlabel))
                h[i].GetXaxis().SetTitle('DNN_score')
            elif(self.histogram=='H_mass'): #or(self.histogram=='H_mass_ext'))
                #Not normalized
                for j in range(1,h[i].GetNbinsX()+1):
                    binlabel = (170-70)*(float(j)/(h[i].GetNbinsX())) + 70
                    if(j%2==0):
                        h[i].GetXaxis().SetBinLabel(j, str(binlabel))
                h[i].GetXaxis().SetTitle('H_mass [GeV]')
            else:
                #By default its not normalized
                for j in range(1,h[i].GetNbinsX()+1):
                    binlabel = (binmax-binmin)*(float(j)/(h[i].GetNbinsX())) + binmin
                    h[i].GetXaxis().SetBinLabel(j, str(binlabel))
            h[i].Draw('same')
            legend.AddEntry(h[i],i ,'l')
        legend.SetNColumns(2)
        legend.Draw()
        c.SetGridy(1)
        c.SaveAs(self.generic.analysis_path + '/PostAnalyzer/datacards/Plots/' + self.year + '/' +  self.region + '/' +plot+'_'+self.diagnostic_extension + '_' + self.histogram + '_' + self.region + '_' + self.year + '.pdf')
        
    def plot(self,plots,channels):
        c = ROOT.TCanvas()
        h = {}
        legend = ROOT.TLegend(0.7,0.7,0.9,0.9)
        legend.SetHeader('Samples','C')
        for i in plots:
            for j in channels:
                if(self.histos[i+j]!=0):
                    self.extractData(i,j)
                h[i+j] = self.histos[i+j]
                h[i+j].SetStats(0)
                h[i+j].SetLineColor(self.colors[j])
                h[i+j].SetFillStyle(0)
                h[i+j].SetLineWidth(3)
                h[i+j].SetLineStyle(self.linestyles[i])
                h[i+j].GetXaxis().SetTickSize(0.0)
                h[i+j].SetMarkerStyle(15)
                h[i+j].GetYaxis().SetTitle('Events / bin')
                h[i+j].SetTitle(self.histogram)
                c.cd(1)
                h[i+j].Draw('same')
                legend.AddEntry(h[i+j],i+' '+j ,'l')
        legend.SetNColumns(2)
        legend.Draw()
        c.SetGridy(1)
        c.SaveAs(self.generic.analysis_path + '/PostAnalyzer/datacards/Plots/' + self.year + '/' +  self.region + '/' +'wholePlots'+'_'+self.diagnostic_extension + '_' + self.histogram + '_' + self.region + '_' + self.year + '.pdf')