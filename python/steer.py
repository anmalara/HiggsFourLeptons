#! /usr/bin/env python
from ModuleRunner import ModuleRunner

def main():

    # years = ['UL16postVFP', 'UL17', 'UL18']
    years = ['UL17','UL18']
    # years = ['UL18']

    ModuleName = 'HiggsFourLeptons'

    run_on_samples = []
    # run_on_samples = ['MuonEG_RunD_standard_UL18']

    MR = ModuleRunner(years, ModuleName)
    # MR.CleanWorkdirs()
    # MR.CreateConfigFiles()
    # MR.Split()
    MR.Submit()
    # MR.CheckStatus()
    # MR.Resubmit()
    # MR.RunLocal(run_on_samples=run_on_samples)
    # MR.Merge()
    # MR.MergeRunII()



if __name__ == '__main__':
    print('Start main')
    main()
