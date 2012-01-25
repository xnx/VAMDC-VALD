# -*- coding: utf-8 -*-

RETURNABLES = {\
'BaseURL':'http://vald.astro.uu.se/atoms/tap/',
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
#############################################################
'MethodID':'Method.id',
'MethodCategory':'Method.category',
'MethodDescription':'Method.description',
#############################################################
'AtomStateID':'AtomState.id',
'AtomSymbol':'Atom.name',
'AtomSpeciesID':'Atom.id',
'AtomInchiKey':'Atom.inchikey',
'AtomInchi':'Atom.inchi',
'AtomNuclearCharge':'Atom.atomic',
'AtomIonCharge':'Atom.ion',
'AtomMassNumber':'Atom.massno',
'AtomStateLandeFactor':'AtomState.lande',
'AtomStateLandeFactorUnit':'unitless',
'AtomStateLandeFactorRef':'AtomState.lande_ref_id',
'AtomStateEnergy':'AtomState.energy',
'AtomStateEnergyRef':'AtomState.energy_ref_id',
'AtomStateEnergyUnit':'1/cm',
'AtomStateTotalAngMom':'AtomState.j',
'AtomStateParity':'AtomState.p',
'AtomStateTermLSL':'AtomState.l',
'AtomStateTermS':'AtomState.s',
'AtomStateTermJ1J2':'AtomState.j1j2()',
'AtomStateTermJKJ':'AtomState.jc',
'AtomStateTermJKS':'AtomState.s2',
'AtomStateKappa':'AtomState.k',
#############################################################
'RadTransID':'RadTran.id',
'RadTransSpeciesRef':'RadTran.species_id',
'RadTransWavelength':'RadTran.wave',
'RadTransWavelengthUnit':u'A',
'RadTransWavelengthComment':'Wavelength is for vacuum.',
'RadTransWavelengthRef':'RadTran.wave_ref_id',
'RadTransUpperStateRef':'RadTran.upstate_id',
'RadTransLowerStateRef':'RadTran.lostate_id',
'RadTransMethod':'RadTran.method_return',
#'RadTransProbabilityA':'RadTran.einsteina',
'RadTransProbabilityLog10WeightedOscillatorStrength':'RadTran.loggf',
#'RadTransProbabilityLog10WeightedOscillatorStrengthEval':'RadTran.accur',
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

# custom function
from django.db.models import Q
OPTRANS= {
    '<':  '__lt',
    '>':  '__gt',
    '=':  '__exact',
    '<=': '__lte',
    '>=': '__gte'}
def bothStates(r,op,rhs):
    try:
        op = OPTRANS[op]
        float(rhs)
    except:
        return Q(pk__isnull=True)
    return Q(**{'upstate__energy'+op:rhs}) & Q(**{'lostate__energy'+op:rhs})

def const_test(r,op,*rhs):
    try:                                                                                
        op = OPTRANS[op]
    except:
        return Q(pk__isnull=True)

RESTRICTABLES = {\
'AtomSymbol':'species__name',
'AtomNuclearCharge':'species__atomic',
'IonCharge':'species__ion',
'StateEnergy':bothStates,
'Lower.StateEnergy':'lostate__energy',
'Upper.StateEnergy':'upstate__energy',
'RadTransWavelength':'wave',
'RadTransWavenumber':('wave',invcm2Angstr),
'RadTransFrequency':('wave',Hz2Angstr),
'RadTransEnergy':('wave',eV2Angstr),
'RadTransProbabilityLog10WeightedOscillatorStrength':'loggf',
'RadTransBroadeningNatural':'gammarad',
'RadTransBroadeningPressure':'gammastark',
'MethodCategory':('method_restrict',valdObstype),
#'RadTransProbabilityA':'einsteina'
}
