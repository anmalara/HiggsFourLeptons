import ROOT
import sys
import os
from ModuleRunnerBase import VariablesBase

ROOT.gROOT.SetBatch(1)
class PlotterDNN(VariablesBase):
	def __init__(self):
		VariablesBase.__init__(self)
		self.years = ['UL18']
		self.DataSetTypes = {'DATA': ['Data'],'MC': ['DY','VBF','VV','ggH']}
		self.hfamilies = ['Z1_lowM_H4l','Z1_recoM_Z2_lowM_H4l', 'Z1_recoM_Z2_recoM_H4l','nominal_H4l','4e_H4l','4m_H4l','2m2e_H4l','H_m_reco_H4l']
		self.hnames = ['Z1vsZ2_mass', 'H_mass','HvsZ1_mass','HvsZ2_mass','H_MvsLep1_pt','H_MvsLep2_pt','H_MvsLep3_pt','H_MvsLep4_pt']
		self.path = self.pnfs_path+'/Analyses/HiggsFourLeptons/UL18/HiggsFourLeptons/'
		self.options = 'colz Hist'
		self.save_location_path = self.analysis_path + '/PostAnalyzer/pdfs'
	
	def DrawHist(self, filename, histname,save_loc,save_name):
		c = ROOT.TCanvas("c","MyCanvas",800,600)
		f = ROOT.TFile(filename)
		h2 = f.Get(histname)
		h2.SetMinimum(0)
		h2.SetStats(0)
		h2.Draw(self.options)
		c.SaveAs(save_loc + '/' +save_name)
		f.Close()

	def Plot(self):
	    for DataType, samples in self.DataSetTypes.items():
		    for sample in samples:
			    for year in self.years:
					rootfile = DataType + '__' + sample + '_standard_' + year + '.root' 
					for family in self.hfamilies:
						for hname in self.hnames:
							histname = family + '/' + hname
							path_ = os.path.join(self.save_location_path + '/' + DataType + '/', family)
							if(not os.path.isdir(path_)):
								os.mkdir(path_)
							save_location = self.save_location_path + '/' + DataType +'/'+ family
							save_name = DataType + '__' + sample + '_standard_' + year + '_' + family + '_' + hname + '.pdf'
							self.DrawHist(self.path+'/'+rootfile,histname,save_location,save_name)

def main():
	PlotterDNN().Plot()

if __name__ == '__main__':
	main()
