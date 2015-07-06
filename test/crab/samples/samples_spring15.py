########
# 25 ns
########
#        CRAB task name          DAS name                                                                                                              
samples['25ns_DYJetsToLL']   = ['/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v3/MINIAODSIM',  ['outputFile=treeECALAlignment.root']]
samples['25ns_WJetsToLNu']   = ['/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM',       ['outputFile=treeECALAlignment.root']]

samples['25ns_QCD15to20Ele'] = ['/QCD_Pt-15to20_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM', ['outputFile=treeECALAlignment.root']]
samples['25ns_QCD20to30Ele'] = ['/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM', ['outputFile=treeECALAlignment.root']]
samples['25ns_QCD30to50Ele'] = ['/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM', ['outputFile=treeECALAlignment.root']]
samples['25ns_QCD50to80Ele'] = ['/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM', ['outputFile=treeECALAlignment.root']]
samples['25ns_QCD30toInfDoubleEle'] = ['/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM', ['outputFile=treeECALAlignment.root']]


########
# 50 ns
########
#        CRAB task name          DAS name                                                                                                              
samples['50ns_DYJetsToLL']   = ['/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v2/MINIAODSIM',  ['outputFile=treeECALAlignment.root']]
samples['50ns_WJetsToLNu']   = ['/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring15DR74-Asympt50ns_MCRUN2_74_V9A-v1/MINIAODSIM',       ['outputFile=treeECALAlignment.root']]


########
# Alternative global configuration
########

config.JobType.psetName = '../Dump_MC_cfg.py'
config.Data.outLFNDirBase = '/store/user/amassiro/ECAL/Alignment/test06Jul2015'