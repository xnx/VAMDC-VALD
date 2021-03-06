# -*- coding: utf-8 -*-
from vamdctap.caselessdict import CaselessDict
RETURNABLES = ({\
'NodeID':'starkb',

#atomstate 
'AtomStateID':'AtomState.id',
'AtomSymbol':'Atom.ion.symbol',
'AtomInchi':'Atom.ion.inchi',
'AtomInchiKey':'Atom.ion.inchikey',
'AtomNuclearCharge':'Atom.ion.nuclear_charge',
'AtomSpeciesID':'Atom.particle_ion_id()',
'AtomIonCharge':'Atom.ion.ion_charge',
'AtomStateConfigurationLabel':'Component.config',
'AtomStateTermLabel':'Component.term',
'AtomStateTotalAngMom' : 'AtomState.totalAngularMomentum',
'AtomStateTermLSL':'Component.L',
'AtomStateTermLSS':'Component.S',
'AtomStateTermLSMultiplicity':'Component.LS_multiplicity',
'AtomStateRef':'AtomState.Sources',
'AtomStateTermJKK':'Component.K',
'AtomStateTermJKJ':'Component.J1',

#radiative transition
'RadTransBroadeningPressure':'RadTran',
'RadTransBroadeningPressureLineshapeName':'Lorentzian',
'RadTransBroadeningPressureLineshapeParameterName':'gammaL',
'RadTransBroadeningPressureLineshapeParameterComment':'Broadening.comment',
'RadTransBroadeningPressureLineshapeParameterUnit':'A',
'RadTransBroadeningPressureLineshapeParameter':'Broadening.value',
'RadTransBroadeningPressureEnvironment':'Broadening.environment',

'RadTransShiftingName':'Shifting.name',
'RadTransShiftingParam':'ShiftingParam.value',
'RadTransShiftingParamName':'delta',
'RadTransShiftingParamUnit':'A',
'RadTransShiftingEnv':'Shifting.environment',

'RadTransUpperStateRef':'RadTran.upper_level.id',
'RadTransLowerStateRef':'RadTran.lower_level.id',
'RadTransWavelength':'RadTran.wavelength',
'RadTransWavelengthUnit':'A',
'RadTransRefs':'RadTran.Sources',
'RadTransID':'RadTran.id',

# environments
'EnvironmentID': 'Environment.id',
'EnvironmentTemperature' : 'Environment.temperature.temperature',
'EnvironmentTemperatureUnit' : 'K',
'EnvironmentTotalNumberDensity':'Environment.temperature.transitiondata.density',
'EnvironmentTotalNumberDensityUnit':'1/cm3',
'EnvironmentSpeciesName':'EnvSpecies.particle_ion_name()',
'EnvironmentSpeciesRef': 'EnvSpecies.particle_ion_id()',

#source
'SourceTitle':'Source.encoded_title()',
'SourceAuthorName':'Source.authors_list()',
'SourceCategory':'journal',
'SourceName' : 'Source.journal.encoded_name()',
'SourceVolume' : 'Source.volume',
'SourceYear' : 'Source.publication_year',
'SourceURI': 'Source.ads_reference',
'SourceVolume' : 'Source.volume',
'SourceID' : 'Source.id',

# particle
'ParticleSpeciesID' : 'Particle.particle_ion_id()',
'ParticleName' : 'Particle.particle_ion_name()',
#'ParticleMass' : 'Particle.mass',
#'ParticleMassUnit' : 'Particle.massunit.value',
#'ParticleCharge' : 'Particle.charge',
})

RESTRICTABLES = ({\
'RadTransWavelength':'wavelength',
'AtomSymbol':'target__ion__symbol',
'IonCharge':'target__ion__ion_charge',
'EnvironmentTemperature' : 'temperature',
'EnvironmentTotalNumberDensity':'density'
})
