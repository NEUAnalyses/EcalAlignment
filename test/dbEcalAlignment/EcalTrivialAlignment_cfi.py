import FWCore.ParameterSet.Config as cms

EcalTrivialConditionRetriever = cms.ESSource("EcalTrivialConditionRetriever",
    getEEAlignmentFromFile = cms.untracked.bool(True),
    EEAlignmentFile = cms.untracked.string('EcalValidation/EcalAlignment/test/myEEAlignment_2010.txt'),
    getESAlignmentFromFile = cms.untracked.bool(True),
    ESAlignmentFile = cms.untracked.string('CalibCalorimetry/EcalTrivialCondModules/data/ESAlignment_2010.txt'),
    getEBAlignmentFromFile = cms.untracked.bool(True),
    EBAlignmentFile = cms.untracked.string('EcalValidation/EcalAlignment/test/myEBAlignment_2010.txt')
)
