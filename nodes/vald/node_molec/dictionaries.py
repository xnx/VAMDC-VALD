# -*- coding: utf-8 -*-

RETURNABLES = {\
'NodeID':'vald',
'SourceID':'Source.id',
'SourceAuthorName':'Source.author',
'SourceCategory':'Source.category',
'SourcePageBegin':'Source.pages',
'SourcePageEnd':'Source.pages',
'SourceName':'Source.journal',
'SourceTitle':'Source.title',
'SourceURI':'Source.url',
'SourceVolume':'Source.volume',
'SourceYear':'Source.year',
############################################################
'MethodID':'Method.id',
'MethodCategory':'Method.category',
'MethodDescription':'Method.description',
############################################################
'MoleculeStateID':'MoleculeState.id',
'MoleculeChemicalName':'Molecule.name',
'MoleculeSpeciesID':'Molecule.id',
'MoleculeInchiKey':'Molecule.inchikey',
'MoleculeInchi':'Molecule.inchi',
'MoleculeStateEnergy':'MoleculeState.energy',
'MoleculeStateEnergyRef':'MoleculeState.energy_ref_id',
'MoleculeStateEnergyUnit':'1/cm',
#############################################################
'AtomStateLandeFactor':'AtomState.lande',
'AtomStateLandeFactorUnit':'unitless',
'AtomStateLandeFactorRef':'AtomState.lande_ref_id',
#############################################################
'RadTransSpeciesRef':'RadTran.species_id',
'RadTransComments':'Wavelength is for vacuum.',
'RadTransWavelength':'RadTran.wave',
'RadTransWavelengthUnit':u'A',
'RadTransWavelengthRef':'RadTran.wave_ref_id',
'RadTransFinalStateRef':'RadTran.upstate_id',
'RadTransInitialStateRef':'RadTran.lostate_id',
'RadTransMethod':'RadTran.method.return',
#'RadTransEffectiveLandeFactor':'RadTran.landeff',
#'RadTransEffectiveLandeFactorUnit':'unitless',
#'RadTransEffectiveLandeFactorRef':'RadTran.lande_ref_id',
'RadTransProbabilityLog10WeightedOscillatorStrength':'RadTran.loggf',
#'RadTransProbabilityLog10WeightedOscillatorStrengthAccuracy':'RadTran.accur',
'RadTransProbabilityLog10WeightedOscillatorStrengthUnit':'unitless',
'RadTransProbabilityLog10WeightedOscillatorStrengthRef':'RadTran.loggf_ref_id',
'RadTransBroadeningNaturalLineshapeParameter':'RadTran.gammarad',
'RadTransBroadeningNaturalLineshapeParameterName':'log(gamma)',
'RadTransBroadeningNaturalLineshapeParameterUnit':'cm3/s',
'RadTransBroadeningNaturalRef':'RadTran.gammarad_ref_id',
'RadTransBroadeningNaturalLineshapeName':'lorentzian',
'RadTransBroadeningPressureLineshapeParameter':'RadTran.gammastark',
'RadTransBroadeningPressureLineshapeName':'lorentzian',
'RadTransBroadeningPressureLineshapeParameterName':'log(gamma)',
'RadTransBroadeningPressureLineshapeParameterUnit':'cm3/s',
'RadTransBroadeningPressureRef':'RadTran.gammastark_ref_id',
'RadTransBroadeningPressureEnvironment':'stark',
'RadTransBroadeningPressureComment':'Stark Broadening',
#'RadTransBroadeningPressureLineshapeParameter':'RadTran.getWaals()',
#'RadTransBroadeningPressureLineshapeParameterUnit':'["cm3/s","unitless"]',
#'RadTransBroadeningPressureLineshapeName':'lorentzian',
#'RadTransBroadeningPressureLineshapeParameterName':'["log(gamma)","alpha"]',
#'RadTransBroadeningPressureRef':'RadTran.waals_ref_id',
}

# import the unit converter functions
from vamdctap.unitconv import *

RESTRICTABLES = {\
'AtomSymbol':'species__name',
'AtomNuclearCharge':'species__atomic',
'AtomIonCharge':'species__ion',
'AtomStateEnergy':'upstate__energy',
'RadTransWavelength':'wave',
'RadTransWavenumber':('wave',invcm2Angstr),
'RadTransFrequency':('wave',Hz2Angstr),
'RadTransEnergy':('wave',eV2Angstr),
'RadTransProbabilityLog10WeightedOscillatorStrength':'loggf',
'RadTransBroadeningNatural':'gammarad',
'RadTransBroadeningPressure':'gammastark',
'MethodCategory':('method_restrict',valdObstype)
}

