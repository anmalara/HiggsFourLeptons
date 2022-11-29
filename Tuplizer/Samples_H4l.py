from Samples.SampleContainer_template import *

modes = [['standard'],['pfcands']]
modes = [['standard']]


def Add_Signals_VBF(SampleContainer):
    sample_name = 'VBF_HToZZTo4L_M125'
    DAS_Names = {
        'UL17': '/VBF_HToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
        'UL18': '/VBF_HToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
        }
    nevents_das={
        'UL17':{'xsecs': 1.044, 'das':499000,    'generated':94612.0,    'weighted':6*372396.47124},
        'UL18':{'xsecs': 1.044, 'das':477000,    'generated':80768.0,    'weighted':6*317889.81546},
    }
    Add_MC(SampleContainer, sample_name=sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes)

def Add_Signals_GluGlu(SampleContainer):
    sample_name = 'GluGluHToZZTo4L_M125'
    DAS_Names = {
        'UL17': '/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
        'UL18': '/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM',
        }
    nevents_das={
        'UL17':{'xsecs': 12.18, 'das':998000,    'generated':167943.0,   'weighted':6*4889914.9177},
        'UL18':{'xsecs': 12.18, 'das':940000,    'generated':153857.0,   'weighted':6*4477013.0119},
    }
    Add_MC(SampleContainer, sample_name=sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes)


def Add_DY(SampleContainer):
    sample_name = 'DYJetsToLL_M-50'
    DAS_Names = {
        'UL17': '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
        'UL18': '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
        }
    nevents_das={
        'UL17':{'xsecs': 6104000, 'das':196329377, 'generated':125741.0,   'weighted':1500*2080891944.11},
        'UL18':{'xsecs': 6104000, 'das':196626007, 'generated':124604.0,   'weighted':1500*2057349927.78},
    }
    Add_MC(SampleContainer, sample_name=sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes)

    sample_name = 'DYJetsToLL_M-10to50'
    DAS_Names = {
        'UL17': '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM',
        'UL18': '/DYJetsToLL_M-10to50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
        }
    nevents_das={
        'UL17':{'xsecs': 18610000, 'das':68480179,  'generated':7018.0,     'weighted':9800*7018.0},
        'UL18':{'xsecs': 18610000, 'das':99177236,  'generated':10104.0,    'weighted':9800*332658520.776},
    }
    Add_MC(SampleContainer, sample_name=sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes)


def Add_Diboson(SampleContainer):
    sample_name = 'ZZTo4L'
    DAS_Names = {
        'UL17': '/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2/MINIAODSIM',
        'UL18': '/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM',
        }
    nevents_das={
        'UL17':{'xsecs': 1256, 'das':99388000,  'generated':5286759.0,  'weighted':20*7026087.3928},
        'UL18':{'xsecs': 1256, 'das':99191000,  'generated':5209228.0,  'weighted':20*6924699.5776},
    }
    Add_MC(SampleContainer, sample_name=sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes)


def GetDasName(name,sample,year,run):
    name = name.replace('RUN',run)
    if sample=='DoubleMuon' and year=='UL17' and run=='E': name = name.replace('-v1','-v2')
    if sample=='EGamma'     and year=='UL18' and run=='D': name = name.replace('_GT36-v1','-v2')
    if sample=='SingleMuon' and year=='UL17' and run=='D': name = name.replace('-v1','_GT36-v1')
    if sample=='SingleMuon' and year=='UL17' and run=='F': name = name.replace('-v1','_GT36-v1')
    if sample=='SingleMuon' and year=='UL18' and run=='C': name = name.replace('-v1','-v2')
    return name


def Add_Data_EGamma(SampleContainer):
    sample_name = 'EGamma'
    nevents_das={
        'UL18':{'das':       {'A':339013231,  'B':153822427, 'C':147827904,  'D':752524583,},
                'generated': {'A':43245,      'B':20216,     'C':19340,      'D':75541,},
          },
    }
    DAS_Names = {
        'UL18': '/EGamma/Run2018RUN-UL2018_MiniAODv2_GT36-v1/MINIAOD',
        }
    Add_Data(SampleContainer, sample_name = sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes, transform=GetDasName)


def Add_Data_SingleMuon(SampleContainer):
    sample_name = 'SingleMuon'
    nevents_das={
        'UL17':{'das':       {               'B':136300266, 'C':165652756, 'D':70274947, 'E':154618774, 'F':242140980},
                'generated': {               'B':22497,     'C':36577,     'D':12968,    'E':48404,     'F':88661},
                },
        'UL18':{'das':       {'A':75499908,   'B':35057758,  'C':34565869,   'D':168620231,},
                'generated': {'A':208892,     'B':88743,     'C':95068,      'D':363550,},
          },
    }
    DAS_Names = {
        'UL17': '/SingleMuon/Run2017RUN-UL2017_MiniAODv2-v1/MINIAOD',
        'UL18': '/SingleMuon/Run2018RUN-UL2018_MiniAODv2_GT36-v1/MINIAOD',
        }
    Add_Data(SampleContainer, sample_name = sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes, transform=GetDasName)


def Add_Data_DoubleMuon(SampleContainer):
    sample_name = 'DoubleMuon'
    nevents_das={
        'UL17':{'das':       {              'B':14501767, 'C':49636525, 'D':23075733, 'E':51531477, 'F':79756560},
                'generated': {              'B':33386,    'C':64079,    'D':30531,    'E':126945,   'F':79756560},
                },
        'UL18':{'das':       {'A':241596817,  'B':119918017, 'C':110032072,  'D':513884680,},
                'generated': {'A':85068,      'B':39157,     'C':36578,      'D':146787,},
          },
    }
    DAS_Names = {
        'UL17': '/DoubleMuon/Run2017RUN-UL2017_MiniAODv2-v1/MINIAOD',
        'UL18': '/DoubleMuon/Run2018RUN-UL2018_MiniAODv2_GT36-v1/MINIAOD',
        }
    Add_Data(SampleContainer, sample_name = sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes, transform=GetDasName)


def Add_Data_MuonEG(SampleContainer):
    sample_name = 'MuonEG'
    nevents_das={
        'UL17':{'das':       {              'B':4453465, 'C':15595214, 'D':19043421, 'E':9164365, 'F':25776363},
                'generated': {              'B':6968,    'C':13411,    'D':5888,     'E':18076,   'F':25577},
                },
        'UL18':{'das':       {'A':32958503,   'B':16204062,  'C':15652198,   'D':71947999,},
                'generated': {'A':32195,      'B':18224,     'C':16586,      'D':67668,},
          },
    }
    DAS_Names = {
        'UL17': '/MuonEG/Run2017RUN-UL2017_MiniAODv2-v1/MINIAOD',
        'UL18': '/MuonEG/Run2018RUN-UL2018_MiniAODv2_GT36-v1/MINIAOD',
        }
    Add_Data(SampleContainer, sample_name = sample_name, group_name=sample_name, nevents_das=nevents_das, DAS_Names=DAS_Names, modes=modes, transform=GetDasName)



def Add_Samples_H4L(SampleContainer):
    Add_Signals_VBF(SampleContainer)
    Add_Signals_GluGlu(SampleContainer)
    Add_Diboson(SampleContainer)
    Add_DY(SampleContainer)
    Add_Data_EGamma(SampleContainer)
    Add_Data_SingleMuon(SampleContainer)
    Add_Data_DoubleMuon(SampleContainer)
    Add_Data_MuonEG(SampleContainer)
