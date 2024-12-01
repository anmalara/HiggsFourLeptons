from ModuleRunner_datacards import *

def main():
    print('\t\t\t--- STARTING THE STEER ---')
    years = ['RunII']#,'UL18','RunII']                              !
    names = ['Data','VV','ggH','VBF']#'DYJetsToLL_M-50'             !
    # names = ['DY']
    signals = [0,0,1,1,0]                                  
    Nps = [['Lumi','lnN',[1.11,1.11,1.11]]]
    rates = [0,0,0,1,0]
    #regions = ['nominal','H_m_reco','Z_m_reco']
    histo = 'DNN_score' # H_mass DNN_score                          !
    if(histo=='DNN_score'):
        rateParams = [[1,'[0.0,10]']]
        smearShape = ['DY'] #'DY'
    elif(histo=='H_mass'):
        rateParams = [[0.4,'[0.3,0.5]']]
        smearShape = [] #'DY'
    shapes = ['shapes_fit_s','shapes_prefit']
    smearStatError = [] #'Data'                                      !
    controlRegion = 'Z_m_reco'                                      #!
    controlProcess = 'VV'                                           #!
    rebinning = 5                                                   #!
    
    regions = ['H_m_reco']#,'Z_m_reco','H_m_geq_180', 'nominal']     !
    MR = ModuleRunner(years,names,signals,Nps,rates,rateParams,regions,histo,shapes,smearShape,smearStatError,controlRegion,controlProcess,rebinning)

    MR.create_combine_rootfiles()
    # MR.produce_datacards()
    # MR.merge_datacards()
    # MR.FitDiagnostic()
    # MR.CollectShapes()

if __name__ == '__main__':
    main()