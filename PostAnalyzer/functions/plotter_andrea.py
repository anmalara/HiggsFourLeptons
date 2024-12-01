from __future__ import absolute_import

#import CombineHarvester.CombineTools.plotting as plot
import ROOT
import os

from collections import OrderedDict

ROOT.PyConfig.IgnoreCommandLineOptions = True
ROOT.gROOT.SetBatch(ROOT.kTRUE)

#plot.ModTDRStyle()

class Plotter():
    def __init__(self,year,region,histo,extension,fake):
        self.pathFitDiagnostic = '/user/bhonore/WorkingArea/CMSSW_10_6_28/src/LEAF/HiggsFourLeptons/PostAnalyzer/datacards/datacards/' + year + '/' + region
        self.region = region
        self.year = year
        self.histo = histo
        self.extension = extension
        self.fake = fake
    def plot(self,outputname, first_dir,second_dir = "ch1"):
        canvas = ROOT.TCanvas()
        legend = ROOT.TLegend(0.70, 0.70, 0.90, 0.91, "", "NBNDC")

        fin = ROOT.TFile(self.pathFitDiagnostic + "/fitDiagnosticsTest_" + self.histo + "_" + self.region + "_" + self.year + "_" + self.fake + self.extension + ".root")
        if(self.extension==''):
            second_dir = self.region
        data = fin.Get(first_dir + "/" + second_dir + "/data")

        legend.AddEntry(data, "data", "P")

        hists = OrderedDict()
        hists["tot"] = {"hist": fin.Get(first_dir + "/" + second_dir + "/total"), "color": ROOT.kBlue+2, "leg": "F"}
        hists["bkg"] = {"hist": fin.Get(first_dir + "/" + second_dir + "/total_background"), "color": ROOT.kAzure+10, "leg": "F"} #ROOT.TColor.GetColor(100, 192, 232)
        #hists["sig"] = {"hist": fin.Get(first_dir + "/" + second_dir + "/total_signal"), "color": ROOT.kRed+1, "leg": "L"}

        hists["VV"] = {"hist": fin.Get(first_dir + "/" + second_dir + "/VV"), "color": ROOT.kBlue+10, "leg": "L"}
        if(second_dir!='ch2'):
            #THIS PROCESSES MIGHT NOT BE IN CH2, POTENTIAL ERROR
            hists["VBF"] = {"hist": fin.Get(first_dir + "/" + second_dir + "/VBF"), "color": ROOT.kOrange+1, "leg": "L"}
            hists["ggH"] = {"hist": fin.Get(first_dir + "/" + second_dir + "/ggH"), "color": ROOT.kRed+2, "leg": "L"}        
            #hists["DY"] = {"hist": fin.Get(first_dir + "/" + second_dir + "/DY"), "color": ROOT.kGreen+2, "leg": "L"}


        key_first = list(hists.keys())[0]
        scaleVBF = 5
        maxi=0
        VBFscaled=False #clicker
        for name in hists.keys():
            hist = hists[name]["hist"]
            maxi = hist.GetMaximum()
        
        for name in hists.keys():
            hist = hists[name]["hist"]
            color = hists[name]["color"]
            leg = hists[name]["leg"]
            hist.SetDirectory(0)
            hist.GetXaxis().SetTitle('DNN score')
            hist.GetYaxis().SetTitle('Event / bin')
            hist.GetXaxis().SetRangeUser(0, 20)
            hist.GetYaxis().SetRangeUser(0,35)
            for j in range(1,hist.GetNbinsX()+1):                    
                    if(j<=20)and(j%2==0):
                        binlabel = j                    
                        hist.GetXaxis().SetBinLabel(j, str(5*binlabel))

            if name == "VBF":
                if(hist.GetMaximum() < ((1.0/scaleVBF)*maxi)):
                    hist.Scale(scaleVBF)
                    VBFscaled=True
            if leg=="L":
                hist.SetLineColor(color)
                hist.SetLineWidth(3)
            else:
                hist.SetFillColor(color)
            if name==key_first:

                hist.Draw("HIST")
            else:
                hist.Draw("HISTSAME")
            if((name == "VBF")and(VBFscaled)):
                legend.AddEntry(hist, name+" x "+str(scaleVBF), leg)
            else:
                legend.AddEntry(hist, name, leg)

        data.Draw("PSAME")
        legend.Draw()
        canvas.SaveAs(outputname)
        return hists

    def doPlots(self,secondDir='ch1'):
        ext = "_" + self.histo + "_" + self.region + "_" + self.year + "_" +self.fake + self.extension + '_' + secondDir
        nameresultfolder = 'results' + ext
        if(not os.path.exists(nameresultfolder)):
            os.mkdir(nameresultfolder)
        
        os.chdir(nameresultfolder)
        hists_prefit = self.plot(outputname="prefit" + ext + ".pdf", first_dir = "shapes_prefit",second_dir = secondDir)
        hists_postfit = self.plot(outputname="postfit" + ext + ".pdf", first_dir = "shapes_fit_s",second_dir = secondDir)

        for hname in hists_prefit.keys():
            print(hname, hists_postfit[hname]["hist"].Integral()/hists_prefit[hname]["hist"].Integral())

        nametxt ='FitNormalizationRatios.txt'
        o = open(nametxt,'w')
        for hname in hists_prefit.keys():
            o.write(str(hname) + ' : ' + str(hists_postfit[hname]["hist"].Integral()/hists_prefit[hname]["hist"].Integral()))
            o.write('\n')
        o.close()
        os.chdir('../')

        if(os.path.exists(' ../datacards/Plots/' + self.year + '/' + self.region + '/' + nameresultfolder)):
            print('File already exist')
        command = 'mv ' + nameresultfolder + ' ../datacards/Plots/' + self.year + '/' + self.region + '/'
        os.system(command)
        print('Normalization ratios written at ' + '../datacards/Plots/' + self.year + '/' + self.region + '/' + nameresultfolder)
