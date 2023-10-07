from Samples.SampleContainer_template import *

# modes = [['standard'],['pfcands']]
modes = [['standard']]


def Add_Signals_VBF(SampleContainer):
    sample_name = 'VBF_HToZZTo4L_M125'
    DAS_Names = {
        'UL16preVFP':  '/VBF_HToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM',
        'UL16postVFP': '/VBF_HToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM',
        'UL17':        '/VBF_HToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
        'UL18':        '/VBF_HToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
        }
    nevents_das={
        'UL16preVFP':  {'xsecs': 1.044, 'das':500000, 'generated':500000, 'weighted':1967422.75}, #total events, excluding filter efficiency
        'UL16postVFP': {'xsecs': 1.044, 'das':498000, 'generated':498000, 'weighted':1959629.0}, #total events, excluding filter efficiency
        'UL17':        {'xsecs': 1.044, 'das':499000, 'generated':499000, 'weighted':1962938.25}, #total events, excluding filter efficiency
        'UL18':        {'xsecs': 1.044, 'das':477000, 'generated':477000, 'weighted':1876392.5}, #total events, excluding filter efficiency
    }
    Add_MC(SampleContainer, sample_name=sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes)

def Add_Signals_GluGlu(SampleContainer):
    sample_name = 'GluGluHToZZTo4L_M125'
    DAS_Names = {
        'UL16preVFP':  '/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM',
        'UL16postVFP': '/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM',
        'UL17':        '/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
        'UL18':        '/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM',
        }
    nevents_das={
        'UL16preVFP':  {'xsecs': 12.18, 'das':1000000, 'generated':1000000, 'weighted':28875034.0}, #total events, excluding filter efficiency
        'UL16postVFP': {'xsecs': 12.18, 'das':1000000, 'generated':1000000, 'weighted':28869738.0}, #total events, excluding filter efficiency
        'UL17':        {'xsecs': 12.18, 'das':998000,  'generated':998000, 'weighted':28813888.0}, #total events, excluding filter efficiency
        'UL18':        {'xsecs': 12.18, 'das':940000,  'generated':940000, 'weighted':27139828.0}, #total events, excluding filter efficiency
    }
    Add_MC(SampleContainer, sample_name=sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes)


def Add_DY(SampleContainer):
    sample_name = 'DYJetsToLL_M-50'
    DAS_Names = {
        'UL16preVFP':  '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM',
        'UL16postVFP': '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM',
        'UL17':        '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
        'UL18':        '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
        }
    nevents_das={
        'UL16preVFP':  {'xsecs': 6104000, 'das':90947213,  'generated':90747224, 'weighted':1.54178066842e+12}, #total events, excluding filter efficiency
        'UL16postVFP': {'xsecs': 6104000, 'das':73859224,  'generated':73859224, 'weighted':1.25485540966e+12}, #total events, excluding filter efficiency
        'UL17':        {'xsecs': 6104000, 'das':196329377, 'generated':196219936, 'weighted':3.33541566054e+12}, #total events, excluding filter efficiency
        'UL18':        {'xsecs': 6104000, 'das':196626007, 'generated':196542336, 'weighted':3.3404574761e+12}, #total events, excluding filter efficiency
    }
    Add_MC(SampleContainer, sample_name=sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes)

    sample_name = 'DYJetsToLL_M-10to50'
    DAS_Names = {
        'UL16preVFP':  '/DYJetsToLL_M-10to50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM',
        'UL16postVFP': '/DYJetsToLL_M-10to50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM',
        'UL17':        '/DYJetsToLL_M-10to50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
        'UL18':        '/DYJetsToLL_M-10to50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
        }
    nevents_das={
        'UL16preVFP':  {'xsecs': 18610000, 'das':49632553, 'generated':49632552, 'weighted': 1.67702482125e+12}, #total events, excluding filter efficiency
        'UL16postVFP': {'xsecs': 18610000, 'das':49267069, 'generated':49267068, 'weighted': 1.6645151785e+12}, #total events, excluding filter efficiency
        'UL17':        {'xsecs': 18610000, 'das':95894507, 'generated':164290384, 'weighted': 3.24050773606e+12}, #total events, excluding filter efficiency
        'UL18':        {'xsecs': 18610000, 'das':99177236, 'generated':99177224, 'weighted': 3.35101663642e+12}, #total events, excluding filter efficiency
    }
    Add_MC(SampleContainer, sample_name=sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes)


    sample_name = 'DYJetsToLL_M-10to50_madgraphMLM'
    DAS_Names = {
        'UL16preVFP':  '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM',
        'UL16postVFP': '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM',
        'UL17':        '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM',
        'UL18':        '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM',
        }
    nevents_das={
        'UL16preVFP':  {'xsecs': 18610000, 'das':25799525, 'generated':25799524, 'weighted': 25799524.0}, #total events, excluding filter efficiency
        'UL16postVFP': {'xsecs': 18610000, 'das':23706672, 'generated':23706672, 'weighted': 23706672.0}, #total events, excluding filter efficiency
        'UL17':        {'xsecs': 18610000, 'das':68480179, 'generated':68395872, 'weighted': 68395872.0}, #total events, excluding filter efficiency
        'UL18':        {'xsecs': 18610000, 'das':99288125, 'generated':99288128, 'weighted': 99288128.0}, #total events, excluding filter efficiency
    }
    Add_MC(SampleContainer, sample_name=sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes)

def Add_Diboson(SampleContainer):
    sample_name = 'ZZTo4L'
    DAS_Names = {
        'UL16preVFP':  '/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM',
        'UL16postVFP': '/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM',
        'UL17':        '/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
        'UL18':        '/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
        }
    nevents_das={
        'UL16preVFP':  {'xsecs': 1256, 'das':49691000, 'generated':49691000, 'weighted':65804232.0}, #total events, excluding filter efficiency
        'UL16postVFP': {'xsecs': 1256, 'das':52137000, 'generated':52137000, 'weighted':69036712.0}, #total events, excluding filter efficiency
        'UL17':        {'xsecs': 1256, 'das':99388000, 'generated':99388000, 'weighted':131699944.0}, #total events, excluding filter efficiency
        'UL18':        {'xsecs': 1256, 'das':99191000, 'generated':99137000, 'weighted':131297240.0}, #total events, excluding filter efficiency
    }
    Add_MC(SampleContainer, sample_name=sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes)

    sample_name = 'ggZZTo4e'
    group_name = 'ggZZ'
    DAS_Names = {
        'UL16preVFP':  '/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM',
        'UL16postVFP': '/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM',
        'UL17':        '/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
        'UL18':        '/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
        }
    nevents_das={
        'UL16preVFP':  {'xsecs': -1, 'das':972000, 'generated':972000, 'weighted':972000.0}, #total events, excluding filter efficiency
        'UL16postVFP': {'xsecs': -1, 'das':992608, 'generated':992608, 'weighted':992608.0}, #total events, excluding filter efficiency
        'UL17':        {'xsecs': -1, 'das':997000, 'generated':997000, 'weighted':997000.0}, #total events, excluding filter efficiency
        'UL18':        {'xsecs': -1, 'das':974000, 'generated':974000, 'weighted':974000.0}, #total events, excluding filter efficiency
    }
    Add_MC(SampleContainer, sample_name=sample_name, group_name=group_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes)

    sample_name = 'ggZZTo4mu'
    group_name = 'ggZZ'
    DAS_Names = {
        'UL16preVFP':  '/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM',
        'UL16postVFP': '/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2/MINIAODSIM',
        'UL17':        '/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
        'UL18':        '/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
        }
    nevents_das={
        'UL16preVFP':  {'xsecs': -1, 'das':968675, 'generated':968675, 'weighted':968675.0}, #total events, excluding filter efficiency
        'UL16postVFP': {'xsecs': -1, 'das':997445, 'generated':997445, 'weighted':997445.0}, #total events, excluding filter efficiency
        'UL17':        {'xsecs': -1, 'das':975090, 'generated':975090, 'weighted':975090.0}, #total events, excluding filter efficiency
        'UL18':        {'xsecs': -1, 'das':845232, 'generated':845232, 'weighted':845232.0}, #total events, excluding filter efficiency
    }
    Add_MC(SampleContainer, sample_name=sample_name, group_name=group_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes)

    sample_name = 'ggZZTo4tau'
    group_name = 'ggZZ'
    DAS_Names = {
        'UL16preVFP':  '/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM',
        'UL16postVFP': '/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM',
        'UL17':        '/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
        'UL18':        '/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
        }
    nevents_das={
        'UL16preVFP':  {'xsecs': -1, 'das':497032, 'generated':497032, 'weighted':497032.0}, #total events, excluding filter efficiency
        'UL16postVFP': {'xsecs': -1, 'das':499183, 'generated':499183, 'weighted':499183.0}, #total events, excluding filter efficiency
        'UL17':        {'xsecs': -1, 'das':499000, 'generated':499000, 'weighted':499000.0}, #total events, excluding filter efficiency
        'UL18':        {'xsecs': -1, 'das':493998, 'generated':493998, 'weighted':493998.0}, #total events, excluding filter efficiency
    }
    Add_MC(SampleContainer, sample_name=sample_name, group_name=group_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes)

    sample_name = 'ggZZTo2e2mu'
    group_name = 'ggZZ'
    DAS_Names = {
        'UL16preVFP':  '/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM',
        'UL16postVFP': '/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM',
        'UL17':        '/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
        'UL18':        '/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
        }
    nevents_das={
        'UL16preVFP':  {'xsecs': -1, 'das':500000, 'generated':500000, 'weighted':500000.0}, #total events, excluding filter efficiency
        'UL16postVFP': {'xsecs': -1, 'das':499000, 'generated':499000, 'weighted':499000.0}, #total events, excluding filter efficiency
        'UL17':        {'xsecs': -1, 'das':500000, 'generated':500000, 'weighted':500000.0}, #total events, excluding filter efficiency
        'UL18':        {'xsecs': -1, 'das':500000, 'generated':500000, 'weighted':500000.0}, #total events, excluding filter efficiency
    }
    Add_MC(SampleContainer, sample_name=sample_name, group_name=group_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes)

    sample_name = 'ggZZTo2e2tau'
    group_name = 'ggZZ'
    DAS_Names = {
        'UL16preVFP':  '/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM',
        'UL16postVFP': '/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM',
        'UL17':        '/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
        'UL18':        '/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
        }
    nevents_das={
        'UL16preVFP':  {'xsecs': -1, 'das':500000, 'generated':500000, 'weighted':500000.0}, #total events, excluding filter efficiency
        'UL16postVFP': {'xsecs': -1, 'das':500000, 'generated':500000, 'weighted':500000.0}, #total events, excluding filter efficiency
        'UL17':        {'xsecs': -1, 'das':498000, 'generated':498000, 'weighted':498000.0}, #total events, excluding filter efficiency
        'UL18':        {'xsecs': -1, 'das':500000, 'generated':500000, 'weighted':500000.0}, #total events, excluding filter efficiency
    }
    Add_MC(SampleContainer, sample_name=sample_name, group_name=group_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes)

    sample_name = 'ggZZTo2mu2tau'
    group_name = 'ggZZ'
    DAS_Names = {
        'UL16preVFP':  '/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM',
        'UL16postVFP': '/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1/MINIAODSIM',
        'UL17':        '/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
        'UL18':        '/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
        }
    nevents_das={
        'UL16preVFP':  {'xsecs': -1, 'das':500000, 'generated':500000, 'weighted':500000.0}, #total events, excluding filter efficiency
        'UL16postVFP': {'xsecs': -1, 'das':500000, 'generated':500000, 'weighted':500000.0}, #total events, excluding filter efficiency
        'UL17':        {'xsecs': -1, 'das':500000, 'generated':500000, 'weighted':500000.0}, #total events, excluding filter efficiency
        'UL18':        {'xsecs': -1, 'das':496000, 'generated':496000, 'weighted':496000.0}, #total events, excluding filter efficiency
    }
    Add_MC(SampleContainer, sample_name=sample_name, group_name=group_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes)

def GetDasName(name,sample,year,run):
    name = name.replace('RUN',run)
    if sample=='SingleElectron' and year=='UL16preVFP' and run=='E': name = name.replace('-v2','-v5')
    if sample=='DoubleMuon' and year=='UL16postVFP' and run=='H': name = name.replace('-v1','-v2')
    if sample=='DoubleMuon' and year=='UL16postVFP' and run=='H': name = name.replace('-v1','-v2')
    if sample=='DoubleMuon' and year=='UL17' and run=='E': name = name.replace('-v1','-v2')
    if sample=='EGamma'     and year=='UL18' and run=='D': name = name.replace('-v1','-v2')
    if sample=='SingleMuon' and year=='UL18' and run=='C': name = name.replace('-v2','-v3')
    if sample=='DoubleEG' and year=='UL16preVFP' and run=='B-ver2': name = name.replace('-v1','-v3')
    if sample=='DoubleEG' and year=='UL17' and run=='C': name = name.replace('-v1','-v2')
    if sample=='DoubleEG' and year=='UL17' and run=='F': name = name.replace('-v1','-v2')
    if year=='UL16preVFP' and 'B-ver' in run: name = name.replace('B-ver1-','B-ver1_').replace('B-ver2-','B-ver2_')
    return name


def Add_Data_SingleElectron(SampleContainer):
    sample_name = 'SingleElectron'
    nevents_das={
        'UL16preVFP':   {
            'das':       {'B-ver1':1422819, 'B-ver2':246440440, 'C':97259854, 'D':148167727, 'E':117269446, 'F':61735326,},
            'generated': {'B-ver1':1422819, 'B-ver2':246440416, 'C':97259856, 'D':148167728, 'E':117269448, 'F':61735328},
          },
        'UL16postVFP': {
            'das':       {'F':8858206, 'G':153363109, 'H':129021893,},
            'generated': {'F':8858206, 'G':153363104, 'H':129021888,},
          },
        'UL17': {
            'das':       {'B':60537490, 'C':136637888,  'D':51526521,  'E':102122055,  'F':128467223,},
            'generated': {'B':60537496, 'C':136637888,  'D':51526524,  'E':102122048,  'F':128467216},
          },
    }
    DAS_Names = {
        'UL16preVFP':  '/SingleElectron/Run2016RUN-HIPM_UL2016_MiniAODv2-v2/MINIAOD',
        'UL16postVFP': '/SingleElectron/Run2016RUN-UL2016_MiniAODv2-v2/MINIAOD',
        'UL17':        '/SingleElectron/Run2017RUN-UL2017_MiniAODv2-v1/MINIAOD',
        }
    Add_Data(SampleContainer, sample_name = sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes, transform=GetDasName)


def Add_Data_EGamma(SampleContainer):
    sample_name = 'EGamma'
    nevents_das={
        'UL18': {
            'das':       {'A':339013231,  'B':153822427, 'C':147827904,  'D':752524583,},
            'generated': {'A':339013184,  'B':153822432, 'C':147827904,  'D':752507840,},
          },
    }
    DAS_Names = {
        'UL18': '/EGamma/Run2018RUN-UL2018_MiniAODv2_GT36-v1/MINIAOD',
        }
    Add_Data(SampleContainer, sample_name = sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes, transform=GetDasName)


def Add_Data_SingleMuon(SampleContainer):
    sample_name = 'SingleMuon'
    nevents_das={
        'UL16preVFP': {
            'das':       {'B-ver1':2789243, 'B-ver2':158145722, 'C':67441308, 'D':98017996, 'E':90984718, 'F':57465359},
            'generated': {'B-ver1':2789243, 'B-ver2':158145744, 'C':67441312, 'D':98018000, 'E':90700472, 'F':57340528},
                },
        'UL16postVFP': {
            'das':        {'F':8024195, 'G':149916849, 'H':174035164},
            'generated':  {'F':8024195, 'G':149916832, 'H':174035184},
                },
        'UL17': {
            'das':       {'B':136294038, 'C':167202975, 'D':70354014, 'E':154607963, 'F':242140980},
            'generated': {'B':136294048, 'C':167202976, 'D':70354016, 'E':154607968, 'F':242140976},
                },
        'UL18':{
            'das':       {'A':241605557,  'B':119918017,  'C':110032072,   'D':513884680,},
            'generated': {'A':241605568,  'B':119918016,  'C':110032080,   'D':513884736,},
          },
    }
    DAS_Names = {
        'UL16preVFP':   '/SingleMuon/Run2016RUN-HIPM_UL2016_MiniAODv2-v2/MINIAOD',
        'UL16postVFP':  '/SingleMuon/Run2016RUN-UL2016_MiniAODv2-v2/MINIAOD',
        'UL17':         '/SingleMuon/Run2017RUN-UL2017_MiniAODv2_GT36-v2/MINIAOD',
        'UL18':         '/SingleMuon/Run2018RUN-UL2018_MiniAODv2_GT36-v2/MINIAOD',
        }
    Add_Data(SampleContainer, sample_name = sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes, transform=GetDasName)


def Add_Data_DoubleMuon(SampleContainer):
    sample_name = 'DoubleMuon'
    nevents_das={
        'UL16preVFP': {
            'das':       {'B-ver1':4199947, 'B-ver2':82535526, 'C':27934629, 'D':33861745, 'E':28246946, 'F':17900759},
            'generated': {'B-ver1':4199947, 'B-ver2':82535528, 'C':27934628, 'D':33861748, 'E':28246944, 'F':17900760},
                },
        'UL16postVFP': {
            'das':        {'F':2429162, 'G':45235604, 'H':48912812},
            'generated':  {'F':2429162, 'G':45235604, 'H':48912816},
                },
        'UL17': {
            'das':       {'B':14501767, 'C':49636525, 'D':23075733, 'E':51531477, 'F':79756560},
            'generated': {'B':14501767, 'C':49636524, 'D':23075732, 'E':51531476, 'F':79756560},
                },
        'UL18':{
            'das':       {'A':75499908, 'B':35057758, 'C':34565869,  'D':168620231,},
            'generated': {'A':75499920, 'B':35057756, 'C':34565868,  'D':168564240,},
          },
    }
    DAS_Names = {
        'UL16preVFP':   '/DoubleMuon/Run2016RUN-HIPM_UL2016_MiniAODv2-v1/MINIAOD',
        'UL16postVFP':  '/DoubleMuon/Run2016RUN-UL2016_MiniAODv2-v1/MINIAOD',
        'UL17':         '/DoubleMuon/Run2017RUN-UL2017_MiniAODv2-v1/MINIAOD',
        'UL18':         '/DoubleMuon/Run2018RUN-UL2018_MiniAODv2_GT36-v1/MINIAOD',
        }
    Add_Data(SampleContainer, sample_name = sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes, transform=GetDasName)

def Add_Data_DoubleEG(SampleContainer):
    sample_name = 'DoubleEG'
    nevents_das={
        'UL16preVFP': {
            'das':       {'B-ver1':5686987, 'B-ver2':143073268, 'C':47677856, 'D':53324960, 'E':49877710, 'F':30216940},
            'generated': {'B-ver1':5608682, 'B-ver2':139869264, 'C':47626040, 'D':53302208, 'E':49794640, 'F':30178980},
                },
        'UL16postVFP': {
            'das':        {'F':4360689, 'G':78797031, 'H':85388734},
            'generated':  {'F':4360689, 'G':78797048, 'H':85388776},
                },
        'UL17': {
            'das':       {'B':58088760, 'C':65181125, 'D':25911432, 'E':56241190, 'F':74265012},
            'generated': {'B':56544080, 'C':63271272, 'D':25911418, 'E':56241204, 'F':74264976},
                },
    }
    DAS_Names = {
        'UL16preVFP':   '/DoubleEG/Run2016RUN-HIPM_UL2016_MiniAODv2-v1/MINIAOD',
        'UL16postVFP':  '/DoubleEG/Run2016RUN-UL2016_MiniAODv2-v1/MINIAOD',
        'UL17':         '/DoubleEG/Run2017RUN-UL2017_MiniAODv2-v1/MINIAOD',
        }
    Add_Data(SampleContainer, sample_name = sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes, transform=GetDasName)

def Add_Data_MuonEG(SampleContainer):
    sample_name = 'MuonEG'
    nevents_das={
        'UL16preVFP': {
            'das':       {'B-ver1':225271, 'B-ver2':32727796, 'C':15405678, 'D':23482352, 'E':22519303, 'F':14100826},
            'generated': {'B-ver1':225271, 'B-ver2':32727794, 'C':15405678, 'D':23482352, 'E':22519304, 'F':14100826},
                },
        'UL16postVFP': {
            'das':        {'F':1901339, 'G':33854612, 'H':29236516},
            'generated':  {'F':1901339, 'G':33854612, 'H':29236516},
                },
        'UL17': {
            'das':       {'B':4453465, 'C':15595214, 'D':9164365, 'E':19043421, 'F':25776363},
            'generated': {'B':4453465, 'C':15198560, 'D':9164365, 'E':19043420, 'F':25776364},
                },
        'UL18':{
            'das':       {'A':32958503,  'B':16204062,  'C':15652198,   'D':71947999,},
            'generated': {'A':32958502,  'B':16204062,  'C':15652198,   'D':71948000,},
          },
    }
    DAS_Names = {
        'UL16preVFP':   '/MuonEG/Run2016RUN-HIPM_UL2016_MiniAODv2-v2/MINIAOD',
        'UL16postVFP':  '/MuonEG/Run2016RUN-UL2016_MiniAODv2-v2/MINIAOD',
        'UL17':         '/MuonEG/Run2017RUN-UL2017_MiniAODv2-v1/MINIAOD',
        'UL18':         '/MuonEG/Run2018RUN-UL2018_MiniAODv2_GT36-v1/MINIAOD',
        }
    Add_Data(SampleContainer, sample_name = sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes, transform=GetDasName)



def Add_Samples_H4L(SampleContainer):
    Add_Signals_VBF(SampleContainer)
    Add_Signals_GluGlu(SampleContainer)
    Add_Diboson(SampleContainer)
    Add_DY(SampleContainer)
    Add_Data_SingleElectron(SampleContainer)
    Add_Data_EGamma(SampleContainer)
    Add_Data_SingleMuon(SampleContainer)
    Add_Data_DoubleMuon(SampleContainer)
    Add_Data_DoubleEG(SampleContainer)
    Add_Data_MuonEG(SampleContainer)
