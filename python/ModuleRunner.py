
import os
from printing_utils import green, blue, prettydict
from utils import ensureDirectory
from parallelize import parallelize
from CreateConfigFiles import CreateConfigFiles
from Samples.Sample import SampleContainer
from HiggsFourLeptons.Tuplizer.Samples_H4l import Add_Samples_H4L
from ModuleRunnerBase import VariablesBase, ModuleRunnerBase

class ModuleRunner(VariablesBase):
    ''' Class container for list of objects for particular year '''
    def __init__(self, years, ModuleName):
        VariablesBase.__init__(self)
        self.years = years
        self.ModuleName = ModuleName
        self.ncores = 4
        print(self)

    def __str__(self):
        print(blue('--> ModuleRunner info:'))
        prettydict(self.__dict__)
        return blue('--> ModuleRunner info: end.')

    def CompileCode(self):
        os.system('cd '+self.analysis_path+'; make -j 4; cd -')

    def CreateConfigFiles(self):
        AllSamples = SampleContainer()
        Add_Samples_H4L(AllSamples)
        xmlfilename = os.path.join(self.config_path,self.ModuleName+'Config.xml')
        CCF = CreateConfigFiles(xmlfilename= xmlfilename, years = self.years, AllSamples=AllSamples)
        CCF.modifyAllSettings()

    def RunAnalyser(self, options):
        commands = []
        path = os.path.join(self.config_path, 'workdir_'+self.ModuleName)
        for year in self.years:
            xmlfilename = os.path.join(self.config_path, 'workdir_'+self.ModuleName, self.ModuleName+'Config_'+year+'.xml')
            commands.append([path, 'submit.py %s -%s' %(xmlfilename, options)])
        a = parallelize(commands, ncores=self.ncores, cwd=True, remove_temp_files=False)

    def CleanWorkdirs(self):
        self.RunAnalyser(options='c')

    def Split(self):
        self.RunAnalyser(options='d')

    def Submit(self):
        self.CompileCode()
        self.RunAnalyser(options='s')

    def Resubmit(self):
        self.RunAnalyser(options='s')

    def CheckStatus(self):
        self.RunAnalyser(options='o')

    def Merge(self):
        # self.RunAnalyser(options='f')
        self.RunAnalyser(options='ift')
        # self.RunAnalyser(options='p')

    def RunLocal(self,ncores=4, run_on_samples=[]):
        import glob
        if not ncores:
            ncores = self.ncores
        if len(run_on_samples)==0:
            run_on_samples = ['']
        print(green('--> Locally running jobs on %i cores' % (ncores)))
        commands = []
        path = os.path.join(self.config_path, 'workdir_'+self.ModuleName)
        for year in self.years:
            for missing_files in glob.glob(os.path.join(self.config_path, 'workdir_'+self.ModuleName, 'workdir_'+self.ModuleName+'Config_'+year,'*','commands_missing_files.txt')):
                with open(missing_files, 'r') as f:
                    for l in f.readlines():
                        commands.append(l.rstrip('\n'))
        commands = [[self.config_path, c] for c in commands if any(x in c for x in run_on_samples)]
        parallelize(commands, ncores=ncores, cwd=True)
        print(green('--> Finished running missing jobs locally.'))

    def MergeGroups(self):
        commands = []
        for year in self.years:
            dir = os.path.join(self.analysis_outpath,year,self.ModuleName)
            for group, info in self.groups.items():
                type, samples = info
                new_file = os.path.join(dir,type+'__'+group+self.PrefixrootFile+year+'.root')
                command = ['hadd', '-f', new_file]
                for sample in samples:
                    if type=='DATA':
                        for run in self.RunPeriods_Dict[year]:
                            fname = new_file.replace(group,sample+'_Run'+run)
                            if os.path.exists(fname):
                                command.append(fname)
                    else:
                        fname = new_file.replace(group,sample)
                        if os.path.exists(fname):
                            command.append(fname)
                if len(command)==4:
                    command = ['cp',command[-1],command[2]]
                commands.append(command)
        parallelize(commands, ncores=4, remove_temp_files=False)

    def MergeRunII(self):
        runII_dir = os.path.join(self.analysis_outpath,'RunII',self.ModuleName)
        ensureDirectory(runII_dir)
        commands = []
        for group, info in self.groups.items():
            for sample in samples:
                type, samples = info
                # for mode in ['','_standard_RunII']:
                for mode in ['_standard_RunII']:
                    new_file = os.path.join(runII_dir,'MC__'+sample+mode+'.root')
                    command = ['hadd', '-f', new_file]
                    for year in self.years:
                        command.append(new_file.replace('RunII',year))
                    commands.append(command)
        parallelize(commands, ncores=4, remove_temp_files=False)
