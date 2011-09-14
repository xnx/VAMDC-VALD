<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0" xmlns:xsams="http://vamdc.org/xml/xsams/0.2">
    
    <xsl:output method="text" indent="no"/>
    
    <xsl:key name="atomicState" match="/xsams:XSAMSData/xsams:Species/xsams:Atoms/xsams:Atom/xsams:Isotope/xsams:Ion/xsams:AtomicState" use="@stateID"/>
    <xsl:key name="molecularState" match="/xsams:XSAMSData/xsams:Species/xsams:Molecules/xsams:Molecule/xsams:MolecularState" use="@stateID"/>

    <xsl:variable name="newline"><xsl:text>
</xsl:text></xsl:variable>

    <xsl:template match="/xsams:XSAMSData/xsams:Processes/xsams:Radiative">
        <xsl:apply-templates/>
    </xsl:template>
    <xsl:template match="xsams:RadiativeTransition" xsl:space="default">
        <xsl:variable name="initialStateId" select="xsams:InitialStateRef"/>
        <xsl:variable name="finalStateId" select="xsams:FinalStateRef"/>
                <xsl:variable name="initialState" select="key('atomicState', $initialStateId)"/>
                <xsl:variable name="finalState" select="key('atomicState', $finalStateId)"/>
                <xsl:value-of select="$initialState/../../../xsams:ChemicalElement/xsams:ElementSymbol"/>, <xsl:value-of select="$initialState/../xsams:IonCharge"/>, <xsl:value-of select="./xsams:EnergyWavelength/xsams:Wavelength/xsams:Value"/>, <xsl:value-of select="$initialState/xsams:AtomicNumericalData/xsams:StateEnergy/xsams:Value"/>, <xsl:value-of select="$finalState/xsams:AtomicNumericalData/xsams:StateEnergy/xsams:Value"/>, <xsl:value-of select="./xsams:Probability/xsams:Log10WeightedOscillatorStrength/xsams:Value"/><xsl:value-of select="$newline"/>
    </xsl:template>
    <xsl:template match="text()|@*"/>
</xsl:stylesheet>
