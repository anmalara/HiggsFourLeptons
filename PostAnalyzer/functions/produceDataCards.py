import os
from collections import OrderedDict
import re
import ROOT
import copy

class DataCard():
    def __init__(self,name):
        self.name = name
        self.path_datacards = '/ada_mnt/ada/user/bhonore/WorkingArea/CMSSW_10_6_28/src/LEAF/HiggsFourLeptons/PostAnalyzer/datacards'
        self.savepath = ''
        self.region = ''
        self.histo = ''
        self.shapes = []
        self.comments = []
        self.separator = '------------'
        self.processes = []
        self.signalnumber = 0
        self.NPs = []
        self.data = []
        self.rateParams = []
        self.isControlCard = False
        self.ControlRegion = ''
        self.thresholdRateControlHisto = 0.1

    def SelectControlProcesses(self):
        #To call after all 'addRateparam' instances and before 'write'
        #GetVVrate
        rateVV = 0
        for i in range(len(self.processes)):                                                #Could be more optimal but requires to change code structure
            if(self.processes[i][1]=='VV'):                                                 #Make VV general
                rateVV=self.processes[i][3]
        procCopy = copy.deepcopy(self.processes)
        for j in range(len(procCopy)):
            if(procCopy[j][3] < self.thresholdRateControlHisto*rateVV):
                rem_ind = j-(len(procCopy)-len(self.processes))#translates indices to the list where we remove
                print('Removing process in control region : ', self.processes[j-(len(procCopy)-len(self.processes))])
                self.processes.pop(rem_ind)
                for i in self.NPs:
                    i[2].pop(rem_ind)
                for i in self.rateParams:
                    if(i[2]==self.processes[j][1]):
                        self.rateParams.remove(i)
                self.shapes.pop(rem_ind+1)#+1 because data in shapes but not in processes
    def addNP(self,npname,scaletype,values):
        assert(len(values)==len(self.processes))
        self.NPs.append([npname,scaletype,values])
    
    def addRateParam(self,bin,process,initval,range):
        self.rateParams.append(['rateParam',bin,process,initval,range])

    def addProcess(self,bin,process,rate,isSignal):
        label = len(self.processes)+1
        if(isSignal):
            label = -self.signalnumber
            self.signalnumber += 1
        else:
            label -= self.signalnumber
        if(process=='Data'):
            self.data = [bin,rate]
        else:
            proc = [bin,process,label,rate]
            self.processes.append(proc)
        
    def add_shape(self,year,sample,region,histo,rootfile,fake):
        #This function is called from extractData_fromFile
        histName = histo + '_' + region + '_' + sample + '_' + year + '_' + fake
        if(sample=='Data'):
            sample = 'data_obs'
        #     histName += '_IsSmeared_Staterror'
        
        # elif(sample=='DY'):
        #     histName += '_IsSmeared_Shape'
        # else:
        #     histName += '_NotSmeared'
        self.shapes.append([sample,region,rootfile,histName])

    def align(self,tabels):
        ret = []
        length = len(tabels[0])
        for j in range(length):
            ret.append([])
            for i in tabels:
                assert(length==len(i))
                ret[-1].append(i[j])
        return ret

    def extractData_fromFile(self,rootfile,isSignal=False):
        prefix,histo,region,sample,year,fake = re.split('-', rootfile,maxsplit=6)
        self.histo = histo
        self.region = region
        #update path to find the datacard
        self.savepath = self.path_datacards + '/datacards/' + year + '/' + region
        if(sample=='Data'):
            if(len(self.data)!=0):
                print('ERROR : multiple data process entries')
            else:
                self.data = [region,sample,year]
        fname = self.path_datacards + '/rootfiles_for_datacards/' + year + '/' + region + '/' + rootfile + '.root'

        if(os.path.exists(fname)):
            f = ROOT.TFile(fname)
            histname = histo + '_' + region + '_' + sample + '_' + year + '_' + fake #According to rootfile production
            hist = f.Get(histname)
            rate = round(hist.Integral(),3)
            self.addProcess(region,sample,rate,isSignal)
            self.add_shape(year,sample,region,histo,fname,fake)
        else:
            print('ERROR : ',fname,' doesnt exist')

    def write(self):
        datacardpath = self.savepath + '/datacard_' + self.histo + '_' + self.name + '' + '.txt'
        try:
            o = open(datacardpath,'w')
        except OSError:
            print('The file at ',self.path + '_' + self.name,' does not exist.')
        #Processes
        o.write('imax\t 1\n')
        o.write('jmax\t ' + str(len(self.processes)-1) + '\n')       
        o.write('kmax\t ' + str(len(self.NPs)) + '\n')
        o.write('--------\n')
        #Shapes
        for shape in self.shapes:
            o.write('shapes\t ' + str(shape[0]) + '\t' + str(shape[1]) + '\t' + str(shape[2]) + '\t' + str(shape[3]) + '\n')
        #Data observation
        o.write('--------\n')
        o.write('bin\t ' + str(self.data[0]) + '\n')
        o.write('observation\t ' + str(self.data[1]) + '\n')
        o.write('--------\n')

        aligned = self.align(self.processes)
        o.write('bin\t ')
        for i in aligned[0]:
            o.write(str(i) + '\t')
        o.write('\n')
        o.write('process\t ')
        for i in aligned[1]:
            o.write(str(i) + '\t')
        o.write('\n')
        o.write('process\t ')
        for i in aligned[2]:
            o.write(str(i) + '\t')
        o.write('\n')
        o.write('rate\t ')
        for i in aligned[3]:
            o.write(str(i) + '\t')
        o.write('\n')
        o.write('--------\n')
        #NP
        for i in self.NPs:
            li = [i[1]]
            for j in i[2]:#range(len(self.processes)):
                li.append(j)
            o.write(str(i[0]) + '\t ')
            for a in li:
                o.write(str(a) + ' ')
            o.write('\n')
        o.write('--------\n')
        #RateParam
        for i in range(len(self.rateParams)):
            o.write('alpha\t ')
            for a in self.rateParams[i]:
                o.write(str(a) + ' ')

        print('---> Datacard written at {}'.format(datacardpath))
        o.close()

def produceDataCard(year,region,histo,names,signals,Nps,RateParams,rates,smearStatError, smearShape, ControlRegion='',fake='FD'):
    if(ControlRegion!=''):
        print(region + '_' + year + '_ControlRegion_' + ControlRegion + '_' + fake)
        d = DataCard(region + '_' + year + '_ControlRegion_' + ControlRegion + '_' + fake)
        d.isControlCard = True
        d.ControlRegion = ControlRegion
    else:
        print(region + '_' + year + '_ControlRegion_' + ControlRegion + '_' + fake)
        d = DataCard(region + '_' + year + '_' + fake)
        d.isControlCard = False
        d.ControlRegion = ''
    if((region=='H_m_geq_180')and(histo=='H_mass')):
        histo = 'H_mass_ext'
    for i in range(len(names)):
        rootfile = 'histograms-' + histo + '-' + region + '-' + names[i] + '-' + year
        if(names[i] in smearStatError):
            rootfile += '-IsSmeared_Staterror'
        elif(names[i] in smearShape):
            rootfile += '-IsSmeared_Shape'
        else:
            rootfile += '-NotSmeared'
        d.extractData_fromFile(rootfile,signals[i])
        if(rates[i]):
            param = RateParams[len(d.rateParams)]
            d.addRateParam(region,names[i],str(param[0]),param[1])
    for i in Nps:
        np = copy.deepcopy(i)
        d.addNP(np[0],np[1],np[2])
    if(d.isControlCard):
            d.SelectControlProcesses()
   
    d.write()

class DataCardMerger():
    def __init__(self):
        self.path_datacards = '/ada_mnt/ada/user/bhonore/WorkingArea/CMSSW_10_6_28/src/LEAF/HiggsFourLeptons/PostAnalyzer/datacards/datacards'
        self.pathsCards = []
        self.outputname = ''

    def addCard(self,histo,region,year,controlRegion='',fake='FD'):
        path = self.path_datacards + '/' + year + '/' + region + '/datacard_' + histo + '_' + region + '_' + year
        if(controlRegion!=''):
            path += '_ControlRegion_' + controlRegion
        path += '_'
        path += fake
        path += '.txt'
        if(len(self.pathsCards)==0):
            self.outputname = self.path_datacards + '/' + year + '/' + region + '/datacard_' + histo + '_' + region + '_' + year + '_' + fake + '_constrained.txt'
        self.pathsCards.append(path)
        
    def merge(self):
        command = 'combineCards.py '
        for i in self.pathsCards:
            command += (i + ' ')
        command += ('> ' + self.outputname)
        print(command)
        os.system(command)
        print(str(len(self.pathsCards)) + ' datacards merged successfully.')