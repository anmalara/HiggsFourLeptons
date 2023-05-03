#! /usr/bin/env python

from ModuleRunnerBase import *
from Submitter.CreateConfigFilesBase import *
from HiggsFourLeptons.Tuplizer.Samples_H4l import *
from Utils import *

class CreateConfigFiles(VariablesBase, CreateConfigFilesBase):
    def __init__(self, xmlfilename, years, AllSamples):
        VariablesBase.__init__(self)
        CreateConfigFilesBase.__init__(self, xmlfilename=xmlfilename, xmlfilepath=self.config_path, years=years, AllSamples=AllSamples)

        self.yearDepententVariables = {
            'LumiblockFile': {
                'UL16preVFP':  'data/UL16/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.root',
                'UL16postVFP': 'data/UL16/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.root',
                'UL17':        'data/UL17/Cert_294927-306462_13TeV_UL2017_Collisions17_GoldenJSON.root',
                'UL18':        'data/UL18/Cert_314472-325175_13TeV_Legacy2018_Collisions18_JSON.root',
            }
        }

    def modifySpecificSettings(self,year):
        self.modifyConfigAttribute('TargetLumi',  ROOT.Year2Lumi[year])
        self.modifyConfigAttribute('JEC_Version', ROOT.JERC_Info[year]['JEC_Version'])
        self.modifyConfigAttribute('JER_Version', ROOT.JERC_Info[year]['JER_Version'])
        self.modifyConfigAttribute('LumiblockFile', self.yearDepententVariables['LumiblockFile'][year])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('xmlfilename', type=str, help='Name of the XML file')
    parser.add_argument("--years", nargs="+", default=ROOT.Reco2Years['UL'], help='Years to run over')

    args = parser.parse_args()
    xmlfilename = args.xmlfilename
    years       = args.years

    years = ['UL16postVFP', 'UL17', 'UL18']

    AllSamples = SampleContainer()
    Add_Samples_H4L(AllSamples)

    CCF = CreateConfigFiles(xmlfilename= xmlfilename, years = years, AllSamples=AllSamples)
    CCF.modifyAllSettings()

if __name__ == '__main__':
    main()
