from createCombineRootFiles import *
from printing_utils import green, blue, prettydict
from collectShapesFromCombine import *
from plotter_andrea import *

#The above is to comment if /ada_mnt/ada/user/bhonore/WorkingArea/CMSSW_11_3_4/src/HiggsAnalysis/CombinedLimit is used
from produceDataCards import *
import os

class ModuleRunner():
    def __init__(self,years,names,signals,Nps,rates,rateParams,regions,histo,shapes,smearShape,smearStatError,controlRegion,controlProcess,rebinning):
        self.years = years
        self.names = names
        self.signals = signals
        self.Nps = Nps
        self.regions = regions
        self.histo = histo
        self.rateParams = rateParams
        self.rates = rates
        self.shapes = shapes
        self.smearShape = smearShape
        self.smearStatError = smearStatError
        self.rebinning = rebinning
        self.path = '/ada_mnt/ada/user/bhonore/WorkingArea/CMSSW_10_6_28/src/LEAF/HiggsFourLeptons/PostAnalyzer/functions'
        self.controlRegion = controlRegion
        self.controlProcess = controlProcess
        if(('Data' not in smearStatError)and('Data' not in smearShape)):
            self.fake = 'RD'
        else: 
            self.fake = 'FD'

    def create_combine_rootfiles(self):
        print(blue('Creating the combine rootfiles'))
        for year in self.years:
            for region in self.regions:
                #Only create smeared data out of non data files
                names_temp = [x for x in self.names if x != 'Data']
                CreateFakeData(year,names_temp,region,self.histo,self.rebinning,250)     
                #create rootfile for fitting           
                for name in self.names:
                    createCombineRootFiles(year,name,region,self.histo,True,self.rebinning)
        print(green('All rootfiles were created successfully'))


    def produce_datacards(self):
        print(blue('Producing the datacards'))
        for year in self.years:
            produceDataCard(year,self.controlRegion,self.histo,self.names,self.signals,self.Nps,self.rateParams,self.rates,self.smearStatError,self.smearShape,self.controlProcess,self.fake)
            for region in self.regions:
                produceDataCard(year,region,self.histo,self.names,self.signals,self.Nps,self.rateParams,self.rates,self.smearStatError,self.smearShape,'',self.fake)     
                #Produce control region datacards
                
        print(green('All datacards were created successfully'))

    def merge_datacards(self):                    
        print('Initializing Datacard Merger')
        for year in self.years:
            for region in self.regions:
                m = DataCardMerger()
                m.addCard(self.histo,region,year,'',self.fake)
                m.addCard(self.histo,self.controlRegion,year,self.controlProcess,self.fake)
                m.merge()
    
    def FitDiagnostic(self):
        print('Starting the Fit Diagnostic')
        for year in self.years:
            for region in self.regions:
                if((region=='H_m_geq_180')and(self.histo=='H_mass')):
                    histogram = 'H_mass_ext'
                else:
                    histogram = self.histo

                #Run combine
                
                dataname = histogram + '_' + region + '_' + year + '_' + self.fake

                os.chdir('../datacards/datacards/' + year + '/' + region + '/')

                #CONSTRAINED FIT
                command = 'combine datacard_' + dataname + '_constrained.txt' + ' -M FitDiagnostics --saveShapes --saveNormalizations --rMax 2'# --bypassFrequentistFit'   + '../../../' + datacard_path + 
                print(command)
                os.system(command)
                print('Constrained Fit Diagnostic successful')
                print('Changing the names of the outputs')

                #Renaming the outputs
                command = 'mv fitDiagnosticsTest.root fitDiagnosticsTest_' + dataname + '_constrained.root'
                os.system(command)
                command = 'mv higgsCombineTest.FitDiagnostics.mH120.root higgsCombineTest.FitDiagnostics.mH120_' + dataname  + '_constrained.root'
                os.system(command)
                command = 'mv combine_logger.out combine_logger_' + dataname  + '_constrained.out'
                os.system(command)
                print('Name change successul')

                #UNCONSTRAINED FIT
                command = 'combine datacard_' + dataname  + '.txt' + ' -M FitDiagnostics --saveShapes --saveNormalizations --rMax 2'# --bypassFrequentistFit'   + '../../../' + datacard_path + 
                print(command)
                os.system(command)
                print('Unconstrained Fit Diagnostic successful')
                print('Changing the names of the outputs')
                #Renaming the outputs
                command = 'mv fitDiagnosticsTest.root fitDiagnosticsTest_' + dataname  + '.root'
                os.system(command)
                command = 'mv higgsCombineTest.FitDiagnostics.mH120.root higgsCombineTest.FitDiagnostics.mH120_' + dataname  + '.root'
                os.system(command)
                command = 'mv combine_logger.out combine_logger_' + dataname  + '.out'
                os.system(command)
                print('Name change successul')

                os.chdir('../../../../functions/')

    def CollectShapes(self):
        print(blue('Collecting the shapes'))
        for year in self.years:
            for region in self.regions:
                if((region=='H_m_geq_180')and(self.histo=='H_mass')):
                    histogram = 'H_mass_ext'
                else:
                    histogram = self.histo
                #Plot unconstrained fits
                p = Plotter(year,region,histogram,'',self.fake)
                p.doPlots()
                #Plot constrained fits
                p_ = Plotter(year,region,histogram,'_constrained',self.fake)
                p_.doPlots('ch1')
                p_.doPlots('ch2')
                
        print(green('Shapes collected'))
    def clearPlots(self):
        os.chdir('../datacards/datacards/Plots/')
        regions = ['H_m_reco','nominal','Z_m_reco','H_m_geq_180']
        years = ['UL17','UL18','RunII']
        for year in self.years:
            for region in self.regions:
                os.chdir(self.path+'/../datacards/Plots/'+year+'/'+region)
                print(os.path())
                
