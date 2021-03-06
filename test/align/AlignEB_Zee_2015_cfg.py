import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.inputTree = cms.PSet(
  nameTree = cms.string("ntupleEcalAlignment/myTree"),
   
   
  #selection = cms.string("(electrons_classification==0 && ETSC>20)"),
  #selection = cms.string("(electrons_classification==0 && ETSC>30) && ((abs(eta) <= 1.5 && (eleTrkIso + eleEcalIso + eleHcalIsoD1 + eleHcalIsoD2)/pT < 0.07 && abs(SigmaIEtaIEta)<0.01) || (abs(eta) >= 1.5 && (eleTrkIso + eleEcalIso + eleHcalIsoD1 + eleHcalIsoD2)/pT < 0.06 && abs(SigmaIEtaIEta)<0.03))"),
  selection = cms.string("(electrons_classification==0 && ETSC>20) && mll<95 && mll>85  && ((abs(eta) <= 1.5 && (eleTrkIso + eleEcalIso + eleHcalIsoD1 + eleHcalIsoD2)/pT < 0.07 && abs(SigmaIEtaIEta)<0.01) || (abs(eta) >= 1.5 && (eleTrkIso + eleEcalIso + eleHcalIsoD1 + eleHcalIsoD2)/pT < 0.06 && abs(SigmaIEtaIEta)<0.03))"),
 
 #selection = cms.string("(ETSC>30 && mishits <= 0 ) && ((abs(eta) <= 1.5 && (eleTrkIso + eleEcalIso + eleHcalIsoD1 + eleHcalIsoD2)/pT < 0.07 && abs(SigmaIEtaIEta)<0.01) || (abs(eta) >= 1.5 && (eleTrkIso + eleEcalIso + eleHcalIsoD1 + eleHcalIsoD2)/pT < 0.06 && abs(SigmaIEtaIEta)<0.03))"),
  #selection = cms.string("1"),
  
  #even = cms.untracked.bool(False), # only "odd" events are used
  #odd  = cms.untracked.bool(False), # only "even" events are used
  
  
  
  traslationX = cms.bool(True),
  traslationY = cms.bool(True),
  traslationZ = cms.bool(True),
  rotationPhi   = cms.bool(False),
  rotationTheta = cms.bool(False),
  rotationPsi   = cms.bool(False),

  setRotationPhi   = cms.untracked.double(0),
  setRotationTheta = cms.untracked.double(0),
  setRotationPsi   = cms.untracked.double(0),



  #DetaBias = cms.untracked.string("(x>0.0 && x<1.5)   * (-(0.4e-3)) + (x>1.5 && x<2.0)   * (2.45513e-03*(x-1.75))   + (x>2.0)            * ((6.137825e-04)/2.)   + (x<0.0 && x>-1.5)  * (0.4e-3)   + (x<-1.5 && x>-2.0) * (2.45513e-03*(x+1.75))        + (x<-2.0)           * ((-6.137825e-04)/2.) + y*0"),
  #DetaBias = cms.untracked.string("(x>0.0 && x<1.5)   * (-(0.23e-3)) + (x>1.5 && x<2.0)   * (2.45513e-03*(x-1.75))   + (x>2.0)            * ((6.137825e-04)/2.)   + (x<0.0 && x>-1.5)  * (0.23e-3)   + (x<-1.5 && x>-2.0) * (2.45513e-03*(x+1.75))        + (x<-2.0)           * ((-6.137825e-04)/2.) + y*0"),
  #DphiBias = cms.untracked.string("(y>0)*((x>0.0 && x<1.5)   * (1.46233e-03)  + (x>1.5)            * (2.73084e-03)  + (x<0.0 && x>-1.5)  * (6.59298e-04)  + (x<-1.5)           * (2.57010e-03)) + \
                                   #(y<0)*((x>0.0 && x<1.5)   * (-7.24105e-04)  + (x>1.5)            * (-1.992615e-03)  + (x<0.0 && x>-1.5)  * (-1.527137e-03)  + (x<-1.5)           * (-3.437939e-03))"),

   
  # 2016

  #
  DetaBias = cms.untracked.string("    (x>0.0 && x<1.5)   * (-(0.27e-3)) \
                                     + (x>1.5)            * (0.05e-3)  \
                                     + (x<0.0 && x>-1.5)  * (0.17e-3)  \
                                     + (x<-1.5)           * (-(0.01e-3))   \
                                     + y*0"),
    
  DphiBias = cms.untracked.string("(y>0)*    \
                                  ((x>0.0 && x<1.5)   * (1.49e-03)  \
                                 + (x>1.5)            * (1.41e-03)  \
                                 + (x<0.0 && x>-1.5)  * (0.74e-03)  \
                                 + (x<-1.5)           * (1.41e-03)) \
                                 + (y<0)*   \
                                   ((x>0.0 && x<1.5)   * (-0.67e-03) \
                                 + (x>1.5)             * (-1.27e-03) \
                                 + (x<0.0 && x>-1.5)  * (-1.39e-03)  \
                                 + (x<-1.5)           * (-1.25e-03))"),


  #inputFilesPosition    = cms.untracked.string(
         #'myEBAlignment_2010_OLD.txt'
    #),

  inputFiles    = cms.vstring(
          #'root://eoscms.cern.ch//store/user/amassiro/ECAL/Alignment/test13Mar2015/DYToEE_M-50_Tune4C_13TeV-pythia8/crab_DYll/150315_215425/0000/treeECALAlignment_1.root',
          #'root://eoscms.cern.ch//store/user/amassiro/ECAL/Alignment/test13Mar2015/DYToEE_M-50_Tune4C_13TeV-pythia8/crab_DYll/150315_215425/0000/treeECALAlignment_2.root'
          
          #'root://eoscms.cern.ch//eos/cms/store/group/dpg_ecal/alca_ecalcalib/amassiro/ECALAlignment/DATA14Jul2015/SingleElectron/crab_SingleElectron/150715_154047/treeECALAlignment_DATA_oldTrkAlign.root'
          #'file:/tmp/amassiro/treeECALAlignment_DATA_oldTrkAlign.root'
        #/tmp/amassiro/eos/cms/store/group/dpg_ecal/alca_ecalcalib/amassiro/ECALAlignment/DATA22Jul2015AODRAW/SingleElectron/crab_SingleElectron/150721_164215/
          #'file:/tmp/amassiro/dataNewTrk.root'

          #'file:/tmp/amassiro/treeECALnewTrkOldEcal.root'


   #hadd /tmp/amassiro/treeECALAlignment.root \
        #/tmp/amassiro/eos/cms/store/group/dpg_ecal/alca_ecalcalib/amassiro/ECALAlignment/DATA29Aug2015AODAllData/SingleElectron/crab_SingleElectron/150827_143017/treeECALAlignment.root    \
        #/tmp/amassiro/eos/cms/store/group/dpg_ecal/alca_ecalcalib/amassiro/ECALAlignment/DATA29Aug2015AODRAWAllData/SingleElectron/crab_SingleElectron/150826_214823/treeECALAlignment.root  

          'file:/tmp/amassiro/treeECALAlignment.root'

    )
)


process.outputTree = cms.PSet(
   #outputFile = cms.string("myEBAlignment_2015_MCtest.txt")
   #outputFile = cms.string("myEBAlignment_2015_OldTrkAlign.txt")
   #outputFile = cms.string("myEBAlignment_2015_NewTrkAlign.txt")
   #outputFile = cms.string("myEBAlignment_2015_NewTrkAlign_31Aug2015.txt")
   #outputFile = cms.string("myEBAlignment_2015_NewTrkAlign_13Oct2015.txt")
   #outputFile = cms.string("myEBAlignment_2015_NewTrkAlign_23Oct2015.txt")
   #outputFile = cms.string("myEBAlignment_2015_NewTrkAlign_26Oct2015.txt")
   #outputFile = cms.string("myEBAlignment_2016_NewTrkAlign_23May2016.txt")
   #outputFile = cms.string("myEBAlignment_2016_NewTrkAlign_newPix_24May2016.txt")
   outputFile = cms.string("myEBAlignment_2016_NewTrkAlign_newPix_30May2016.txt")
)

