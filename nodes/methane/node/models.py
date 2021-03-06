# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class TransitionTypes(models.Model):
    typeid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=90)
    class Meta:
        db_table = u'transition_types'

class Characterisation(models.Model):
    characid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    class Meta:
        db_table = u'characterisation'

    def renameCharacterisation(self):
        result = self.name
        if(self.characid == 1):
           result = "E2"
        if(self.characid == 2):
           result = "P"
        return result

    def getUnit(self):
        result = self.name
        if(self.characid == 1):
           result = "1/cm2/atm"
        if(self.characid == 2):
           result = "undef"
        return result

class Sources(models.Model):
    sourceid = models.IntegerField(primary_key=True)
    ris = models.TextField()
    class Meta:
        db_table = u'sources'

    def extractChain(self,tokens,st):
        for token in tokens:
            if(token.startswith(st)): break

        result = token[5:]

        if(st == "TY"):
            result={
                "JOUR": "journal",
                "BOOK": "book",
               #"CHAP": "Book chapter",
               #"CONF": "Conference proceeding",
                "":""
            }[result]

        return result

    def author(self,tokens,st):
        a=[]
        for token in tokens:
           if(token.startswith(st)): a.append(token[5:])
        return a

    def extractRisVal(self,st):
        tokens = self.ris.split("|")
        result={
            "TY": self.extractChain(tokens,st),
            "T1": self.extractChain(tokens,st),
            "JO": self.extractChain(tokens,st),
            "VL": self.extractChain(tokens,st),
            "IS": self.extractChain(tokens,st),
            "SP": self.extractChain(tokens,st),
            "EP": self.extractChain(tokens,st),
            "PY": self.extractChain(tokens,st),
            "AU": self.author(tokens,st),
            "M1": self.extractChain(tokens,st),
            "ER": self.extractChain(tokens,st)
        }[st]

        return result

class SymmetryNames(models.Model):
    symnameid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=9)
    class Meta:
        db_table = u'symmetry_names'

class VibrationalLevels(models.Model):
    levelid = models.IntegerField(primary_key=True)
    nbmode = models.IntegerField()
    v1 = models.IntegerField(null=True, blank=True)
    v2 = models.IntegerField(null=True, blank=True)
    v3 = models.IntegerField(null=True, blank=True)
    v4 = models.IntegerField(null=True, blank=True)
    v5 = models.IntegerField(null=True, blank=True)
    v6 = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'vibrational_levels'

class PolyadDescriptions(models.Model):
    poldesid = models.IntegerField(primary_key=True)
    nblev = models.IntegerField()
    levelid1 = models.ForeignKey(VibrationalLevels, null=True, db_column='levelid1', blank=True, related_name='rn_levelid1')
    levelid2 = models.ForeignKey(VibrationalLevels, null=True, db_column='levelid2', blank=True, related_name='rn_levelid2')
    levelid3 = models.ForeignKey(VibrationalLevels, null=True, db_column='levelid3', blank=True, related_name='rn_levelid3')
    levelid4 = models.ForeignKey(VibrationalLevels, null=True, db_column='levelid4', blank=True, related_name='rn_levelid4')
    levelid5 = models.ForeignKey(VibrationalLevels, null=True, db_column='levelid5', blank=True, related_name='rn_levelid5')
    levelid6 = models.ForeignKey(VibrationalLevels, null=True, db_column='levelid6', blank=True, related_name='rn_levelid6')
    levelid7 = models.ForeignKey(VibrationalLevels, null=True, db_column='levelid7', blank=True, related_name='rn_levelid7')
    levelid8 = models.ForeignKey(VibrationalLevels, null=True, db_column='levelid8', blank=True, related_name='rn_levelid8')
    levelid9 = models.ForeignKey(VibrationalLevels, null=True, db_column='levelid9', blank=True, related_name='rn_levelid9')
    levelid10 = models.ForeignKey(VibrationalLevels, null=True, db_column='levelid10', blank=True, related_name='rn_levelid10')
    levelid11 = models.ForeignKey(VibrationalLevels, null=True, db_column='levelid11', blank=True, related_name='rn_levelid11')
    levelid12 = models.ForeignKey(VibrationalLevels, null=True, db_column='levelid12', blank=True, related_name='rn_levelid12')
    levelid13 = models.ForeignKey(VibrationalLevels, null=True, db_column='levelid13', blank=True, related_name='rn_levelid13')
    levelid14 = models.ForeignKey(VibrationalLevels, null=True, db_column='levelid14', blank=True, related_name='rn_levelid14')
    class Meta:
        db_table = u'polyad_descriptions'

class MoleculeTypes(models.Model):
    moltypeid = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=30)
    nbmode = models.IntegerField()
    nbquantumnb = models.IntegerField()
    qname1 = models.CharField(max_length=12)
    status1 = models.IntegerField()
    qname2 = models.CharField(max_length=12)
    status2 = models.IntegerField()
    qname3 = models.CharField(max_length=12)
    status3 = models.IntegerField()
    qname4 = models.CharField(max_length=12)
    status4 = models.IntegerField()
    qname5 = models.CharField(max_length=12)
    status5 = models.IntegerField()
    qname6 = models.CharField(max_length=12)
    status6 = models.IntegerField()
    qname7 = models.CharField(max_length=12)
    status7 = models.IntegerField()
    qname8 = models.CharField(max_length=12)
    status8 = models.IntegerField()
    qname9 = models.CharField(max_length=12)
    status9 = models.IntegerField()
    qname10 = models.CharField(max_length=12)
    status10 = models.IntegerField()
    qname11 = models.CharField(max_length=12)
    status11 = models.IntegerField()
    qname12 = models.CharField(max_length=12)
    status12 = models.IntegerField()
    qname13 = models.CharField(max_length=12)
    status13 = models.IntegerField()
    qname14 = models.CharField(max_length=12)
    status14 = models.IntegerField()
    qname15 = models.CharField(max_length=12)
    status15 = models.IntegerField()
    qname16 = models.CharField(max_length=12)
    status16 = models.IntegerField()
    qname17 = models.CharField(max_length=12)
    status17 = models.IntegerField()
    qname18 = models.CharField(max_length=12)
    status18 = models.IntegerField()
    qname19 = models.CharField(max_length=12)
    status19 = models.IntegerField()
    qname20 = models.CharField(max_length=12)
    status20 = models.IntegerField()
    qname21 = models.CharField(max_length=12)
    status21 = models.IntegerField()
    class Meta:
        db_table = u'molecule_types'

class PolyadSchemes(models.Model):
    polschid = models.IntegerField(primary_key=True)
    moltypeid = models.ForeignKey(MoleculeTypes, db_column='moltypeid')
    nbsublev0 = models.IntegerField()
    poldesid0 = models.ForeignKey(PolyadDescriptions, null=True, db_column='poldesid0', blank=True, related_name='rn_poldesid0')
    nbsublev1 = models.IntegerField()
    poldesid1 = models.ForeignKey(PolyadDescriptions, null=True, db_column='poldesid1', blank=True, related_name='rn_poldesid1')
    nbsublev2 = models.IntegerField()
    poldesid2 = models.ForeignKey(PolyadDescriptions, null=True, db_column='poldesid2', blank=True, related_name='rn_poldesid2')
    nbsublev3 = models.IntegerField()
    poldesid3 = models.ForeignKey(PolyadDescriptions, null=True, db_column='poldesid3', blank=True, related_name='rn_poldesid3')
    nbsublev4 = models.IntegerField()
    poldesid4 = models.ForeignKey(PolyadDescriptions, null=True, db_column='poldesid4', blank=True, related_name='rn_poldesid4')
    nbsublev5 = models.IntegerField()
    poldesid5 = models.ForeignKey(PolyadDescriptions, null=True, db_column='poldesid5', blank=True, related_name='rn_poldesid5')
    nbsublev6 = models.IntegerField()
    poldesid6 = models.ForeignKey(PolyadDescriptions, null=True, db_column='poldesid6', blank=True, related_name='rn_poldesid6')
    nbsublev7 = models.IntegerField()
    poldesid7 = models.ForeignKey(PolyadDescriptions, null=True, db_column='poldesid7', blank=True, related_name='rn_poldesid7')
    nbsublev8 = models.IntegerField()
    poldesid8 = models.ForeignKey(PolyadDescriptions, null=True, db_column='poldesid8', blank=True, related_name='rn_poldesid8')
    nbsublev9 = models.IntegerField()
    poldesid9 = models.ForeignKey(PolyadDescriptions, null=True, db_column='poldesid9', blank=True, related_name='rn_poldesid9')
    class Meta:
        db_table = u'polyad_schemes'

class Polyads(models.Model):
    polyadid = models.IntegerField(primary_key=True)
    polschid = models.ForeignKey(PolyadSchemes, db_column='polschid')
    polyadnb = models.IntegerField()
    class Meta:
        db_table = u'polyads'

class VibrationalSublevels(models.Model):
    sublevid = models.IntegerField(primary_key=True)
    moltypeid = models.ForeignKey(MoleculeTypes, db_column='moltypeid')
    qvalue1 = models.IntegerField()
    qvalue2 = models.IntegerField()
    qvalue3 = models.IntegerField()
    qvalue4 = models.IntegerField()
    qvalue5 = models.IntegerField()
    qvalue6 = models.IntegerField()
    qvalue7 = models.IntegerField()
    qvalue8 = models.IntegerField()
    qvalue9 = models.IntegerField()
    qvalue10 = models.IntegerField()
    qvalue11 = models.IntegerField()
    qvalue12 = models.IntegerField()
    qvalue13 = models.IntegerField()
    qvalue14 = models.IntegerField()
    qvalue15 = models.IntegerField()
    qvalue16 = models.IntegerField()
    qvalue17 = models.IntegerField()
    qvalue18 = models.IntegerField()
    qvalue19 = models.IntegerField()
    qvalue20 = models.IntegerField()
    qvalue21 = models.IntegerField()
    class Meta:
        db_table = u'vibrational_sublevels'

class MoleculesIsotopes(models.Model):
    isotopeid = models.IntegerField(primary_key=True)
    moltypeid = models.ForeignKey(MoleculeTypes, db_column='moltypeid')
    isotopename = models.CharField(max_length=30)
    inchi = models.CharField(max_length=120)
    inchikey = models.CharField(max_length=81)
    class Meta:
        db_table = u'molecules_isotopes'

class ScalarNumbers(models.Model):
    scalarid = models.IntegerField(primary_key=True)
    isotopeid = models.ForeignKey(MoleculesIsotopes, db_column='isotopeid')
    polyadid = models.ForeignKey(Polyads, db_column='polyadid')
    beta = models.FloatField()
    gamma = models.FloatField()
    pi = models.FloatField()
    class Meta:
        db_table = u'scalar_numbers'

class VibrationalComponents(models.Model):
    vibcompid = models.IntegerField(primary_key=True)
    isotopeid = models.ForeignKey(MoleculesIsotopes, db_column='isotopeid')
    polyadid = models.ForeignKey(Polyads, db_column='polyadid')
    sublevid1 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid1', blank=True, related_name='rn_sublevid1')
    coefficient1 = models.FloatField(null=True, blank=True)
    sublevid2 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid2', blank=True, related_name='rn_sublevid2')
    coefficient2 = models.FloatField(null=True, blank=True)
    sublevid3 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid3', blank=True, related_name='rn_sublevid3')
    coefficient3 = models.FloatField(null=True, blank=True)
    sublevid4 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid4', blank=True, related_name='rn_sublevid4')
    coefficient4 = models.FloatField(null=True, blank=True)
    sublevid5 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid5', blank=True, related_name='rn_sublevid5')
    coefficient5 = models.FloatField(null=True, blank=True)
    sublevid6 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid6', blank=True, related_name='rn_sublevid6')
    coefficient6 = models.FloatField(null=True, blank=True)
    sublevid7 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid7', blank=True, related_name='rn_sublevid7')
    coefficient7 = models.FloatField(null=True, blank=True)
    sublevid8 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid8', blank=True, related_name='rn_sublevid8')
    coefficient8 = models.FloatField(null=True, blank=True)
    sublevid9 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid9', blank=True, related_name='rn_sublevid9')
    coefficient9 = models.FloatField(null=True, blank=True)
    sublevid10 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid10', blank=True, related_name='rn_sublevid10')
    coefficient10 = models.FloatField(null=True, blank=True)
    sublevid11 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid11', blank=True, related_name='rn_sublevid11')
    coefficient11 = models.FloatField(null=True, blank=True)
    sublevid12 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid12', blank=True, related_name='rn_sublevid12')
    coefficient12 = models.FloatField(null=True, blank=True)
    sublevid13 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid13', blank=True, related_name='rn_sublevid13')
    coefficient13 = models.FloatField(null=True, blank=True)
    sublevid14 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid14', blank=True, related_name='rn_sublevid14')
    coefficient14 = models.FloatField(null=True, blank=True)
    sublevid15 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid15', blank=True, related_name='rn_sublevid15')
    coefficient15 = models.FloatField(null=True, blank=True)
    sublevid16 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid16', blank=True, related_name='rn_sublevid16')
    coefficient16 = models.FloatField(null=True, blank=True)
    sublevid17 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid17', blank=True, related_name='rn_sublevid17')
    coefficient17 = models.FloatField(null=True, blank=True)
    sublevid18 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid18', blank=True, related_name='rn_sublevid18')
    coefficient18 = models.FloatField(null=True, blank=True)
    sublevid19 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid19', blank=True, related_name='rn_sublevid19')
    coefficient19 = models.FloatField(null=True, blank=True)
    sublevid20 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid20', blank=True, related_name='rn_sublevid20')
    coefficient20 = models.FloatField(null=True, blank=True)
    sublevid21 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid21', blank=True, related_name='rn_sublevid21')
    coefficient21 = models.FloatField(null=True, blank=True)
    sublevid22 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid22', blank=True, related_name='rn_sublevid22')
    coefficient22 = models.FloatField(null=True, blank=True)
    sublevid23 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid23', blank=True, related_name='rn_sublevid23')
    coefficient23 = models.FloatField(null=True, blank=True)
    sublevid24 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid24', blank=True, related_name='rn_sublevid24')
    coefficient24 = models.FloatField(null=True, blank=True)
    sublevid25 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid25', blank=True, related_name='rn_sublevid25')
    coefficient25 = models.FloatField(null=True, blank=True)
    sublevid26 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid26', blank=True, related_name='rn_sublevid26')
    coefficient26 = models.FloatField(null=True, blank=True)
    sublevid27 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid27', blank=True, related_name='rn_sublevid27')
    coefficient27 = models.FloatField(null=True, blank=True)
    sublevid28 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid28', blank=True, related_name='rn_sublevid28')
    coefficient28 = models.FloatField(null=True, blank=True)
    sublevid29 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid29', blank=True, related_name='rn_sublevid29')
    coefficient29 = models.FloatField(null=True, blank=True)
    sublevid30 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid30', blank=True, related_name='rn_sublevid30')
    coefficient30 = models.FloatField(null=True, blank=True)
    sublevid31 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid31', blank=True, related_name='rn_sublevid31')
    coefficient31 = models.FloatField(null=True, blank=True)
    sublevid32 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid32', blank=True, related_name='rn_sublevid32')
    coefficient32 = models.FloatField(null=True, blank=True)
    sublevid33 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid33', blank=True, related_name='rn_sublevid33')
    coefficient33 = models.FloatField(null=True, blank=True)
    sublevid34 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid34', blank=True, related_name='rn_sublevid34')
    coefficient34 = models.FloatField(null=True, blank=True)
    sublevid35 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid35', blank=True, related_name='rn_sublevid35')
    coefficient35 = models.FloatField(null=True, blank=True)
    sublevid36 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid36', blank=True, related_name='rn_sublevid36')
    coefficient36 = models.FloatField(null=True, blank=True)
    sublevid37 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid37', blank=True, related_name='rn_sublevid37')
    coefficient37 = models.FloatField(null=True, blank=True)
    sublevid38 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid38', blank=True, related_name='rn_sublevid38')
    coefficient38 = models.FloatField(null=True, blank=True)
    sublevid39 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid39', blank=True, related_name='rn_sublevid39')
    coefficient39 = models.FloatField(null=True, blank=True)
    sublevid40 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid40', blank=True, related_name='rn_sublevid40')
    coefficient40 = models.FloatField(null=True, blank=True)
    sublevid41 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid41', blank=True, related_name='rn_sublevid41')
    coefficient41 = models.FloatField(null=True, blank=True)
    sublevid42 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid42', blank=True, related_name='rn_sublevid42')
    coefficient42 = models.FloatField(null=True, blank=True)
    sublevid43 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid43', blank=True, related_name='rn_sublevid43')
    coefficient43 = models.FloatField(null=True, blank=True)
    sublevid44 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid44', blank=True, related_name='rn_sublevid44')
    coefficient44 = models.FloatField(null=True, blank=True)
    sublevid45 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid45', blank=True, related_name='rn_sublevid45')
    coefficient45 = models.FloatField(null=True, blank=True)
    sublevid46 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid46', blank=True, related_name='rn_sublevid46')
    coefficient46 = models.FloatField(null=True, blank=True)
    sublevid47 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid47', blank=True, related_name='rn_sublevid47')
    coefficient47 = models.FloatField(null=True, blank=True)
    sublevid48 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid48', blank=True, related_name='rn_sublevid48')
    coefficient48 = models.FloatField(null=True, blank=True)
    sublevid49 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid49', blank=True, related_name='rn_sublevid49')
    coefficient49 = models.FloatField(null=True, blank=True)
    sublevid50 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid50', blank=True, related_name='rn_sublevid50')
    coefficient50 = models.FloatField(null=True, blank=True)
    sublevid51 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid51', blank=True, related_name='rn_sublevid51')
    coefficient51 = models.FloatField(null=True, blank=True)
    sublevid52 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid52', blank=True, related_name='rn_sublevid52')
    coefficient52 = models.FloatField(null=True, blank=True)
    sublevid53 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid53', blank=True, related_name='rn_sublevid53')
    coefficient53 = models.FloatField(null=True, blank=True)
    sublevid54 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid54', blank=True, related_name='rn_sublevid54')
    coefficient54 = models.FloatField(null=True, blank=True)
    sublevid55 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid55', blank=True, related_name='rn_sublevid55')
    coefficient55 = models.FloatField(null=True, blank=True)
    sublevid56 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid56', blank=True, related_name='rn_sublevid56')
    coefficient56 = models.FloatField(null=True, blank=True)
    sublevid57 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid57', blank=True, related_name='rn_sublevid57')
    coefficient57 = models.FloatField(null=True, blank=True)
    sublevid58 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid58', blank=True, related_name='rn_sublevid58')
    coefficient58 = models.FloatField(null=True, blank=True)
    sublevid59 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid59', blank=True, related_name='rn_sublevid59')
    coefficient59 = models.FloatField(null=True, blank=True)
    sublevid60 = models.ForeignKey(VibrationalSublevels, null=True, db_column='sublevid60', blank=True, related_name='rn_sublevid60')
    coefficient60 = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'vibrational_components'

class MolecularStates(models.Model):
    stateid = models.IntegerField(primary_key=True)
    isotopeid = models.ForeignKey(MoleculesIsotopes, db_column='isotopeid')
    polyadid = models.ForeignKey(Polyads, db_column='polyadid')
    position = models.FloatField()
    j = models.IntegerField()
    symnameid = models.ForeignKey(SymmetryNames, db_column='symnameid')
    alpha = models.IntegerField()
    vibcompid = models.ForeignKey(VibrationalComponents, db_column='vibcompid')
    weight = models.IntegerField()
    class Meta:
        db_table = u'molecular_states'

    def PnJcn(self):
        return "P%s %s %s %s" % (self.polyadid.polyadnb,self.j,self.symnameid.name,self.alpha)

#   def getQnLabel(self):
#      #return "('J','rovibSym','r')"
#       return "('J')"
#      #return "'J'"

#   def getQnAttribute(self):
#      #return "('','','name=\"alpha\"')"
#       return "('')"
#      #return ""

#   def getQnValue(self):
#      #return "('%s','%s','%s')" (self.j,self.symnameid.name,self.alpha)
#       return "('%s')" (self.j)
#      #return "'%s'" (self.j)

    def getQNJ(self):
        return "'%s'" (self.j)

    def getQNrovibSym(self):
        return "'%s'" (self.symnameid.name)

    def getQNr(self):
        return "('%s')" (self.alpha)

    def getQNrName(self):
        return "('alpha')"

class Transitions(models.Model):
    transitionid = models.IntegerField(primary_key=True)
    isotopeid = models.ForeignKey(MoleculesIsotopes, db_column='isotopeid')
    typeid = models.ForeignKey(TransitionTypes, db_column='typeid')
    characid = models.ForeignKey(Characterisation, db_column='characid')
    lowstateid = models.ForeignKey(MolecularStates, db_column='lowstateid', related_name='rn_lowstateid')
    upstateid = models.ForeignKey(MolecularStates, db_column='upstateid', related_name='rn_upstateid')
    wavenumber = models.FloatField()
    wavenumber_prec = models.FloatField()
    wavenumber_residual = models.FloatField()
    wavenumber_sourceid = models.ForeignKey(Sources, null=True, db_column='wavenumber_sourceid', blank=True, related_name='rn_wavenumber_sourceid')
    intensity = models.FloatField()
    inthitran = models.FloatField(db_column='intHITRAN') # Field name made lowercase.
    intensity_prec = models.FloatField()
    intensity_residual = models.FloatField()
    intensity_sourceid = models.ForeignKey(Sources, null=True, db_column='intensity_sourceid', blank=True, related_name='rn_intensity_sourceid')
    einstein = models.FloatField()
    gamma1 = models.FloatField()
    gamma1_prec = models.FloatField()
    gamma1_sourceid = models.ForeignKey(Sources, null=True, db_column='gamma1_sourceid', blank=True, related_name='rn_gamma1_sourceid')
    delta1 = models.FloatField()
    delta1_prec = models.FloatField()
    delta1_sourceid = models.ForeignKey(Sources, null=True, db_column='delta1_sourceid', blank=True, related_name='rn_delta1_sourceid')
    nexp1 = models.FloatField()
    nexp1_prec = models.FloatField()
    nexp1_sourceid = models.ForeignKey(Sources, null=True, db_column='nexp1_sourceid', blank=True, related_name='rn_nexp1_sourceid')
    gamma2 = models.FloatField()
    gamma2_prec = models.FloatField()
    gamma2_sourceid = models.ForeignKey(Sources, null=True, db_column='gamma2_sourceid', blank=True, related_name='rn_gamma2_sourceid')
    delta2 = models.FloatField()
    delta2_prec = models.FloatField()
    delta2_sourceid = models.ForeignKey(Sources, null=True, db_column='delta2_sourceid', blank=True, related_name='rn_delta2_sourceid')
    nexp2 = models.FloatField()
    nexp2_prec = models.FloatField()
    nexp2_sourceid = models.ForeignKey(Sources, null=True, db_column='nexp2_sourceid', blank=True, related_name='rn_nexp2_sourceid')
    gamma3 = models.FloatField()
    gamma3_prec = models.FloatField()
    gamma3_sourceid = models.ForeignKey(Sources, null=True, db_column='gamma3_sourceid', blank=True, related_name='rn_gamma3_sourceid')
    delta3 = models.FloatField()
    delta3_prec = models.FloatField()
    delta3_sourceid = models.ForeignKey(Sources, null=True, db_column='delta3_sourceid', blank=True, related_name='rn_delta3_sourceid')
    nexp3 = models.FloatField()
    nexp3_prec = models.FloatField()
    nexp3_sourceid = models.ForeignKey(Sources, null=True, db_column='nexp3_sourceid', blank=True, related_name='rn_nexp3_sourceid')
    gamma4 = models.FloatField()
    gamma4_prec = models.FloatField()
    gamma4_sourceid = models.ForeignKey(Sources, null=True, db_column='gamma4_sourceid', blank=True, related_name='rn_gamma4_sourceid')
    delta4 = models.FloatField()
    delta4_prec = models.FloatField()
    delta4_sourceid = models.ForeignKey(Sources, null=True, db_column='delta4_sourceid', blank=True, related_name='rn_delta4_sourceid')
    nexp4 = models.FloatField()
    nexp4_prec = models.FloatField()
    nexp4_sourceid = models.ForeignKey(Sources, null=True, db_column='nexp4_sourceid', blank=True, related_name='rn_nexp4_sourceid')
    gamma5 = models.FloatField()
    gamma5_prec = models.FloatField()
    gamma5_sourceid = models.ForeignKey(Sources, null=True, db_column='gamma5_sourceid', blank=True, related_name='rn_gamma5_sourceid')
    delta5 = models.FloatField()
    delta5_prec = models.FloatField()
    delta5_sourceid = models.ForeignKey(Sources, null=True, db_column='delta5_sourceid', blank=True, related_name='rn_delta5_sourceid')
    nexp5 = models.FloatField()
    nexp5_prec = models.FloatField()
    nexp5_sourceid = models.ForeignKey(Sources, null=True, db_column='nexp5_sourceid', blank=True, related_name='rn_nexp5_sourceid')
    gamma6 = models.FloatField()
    gamma6_prec = models.FloatField()
    gamma6_sourceid = models.ForeignKey(Sources, null=True, db_column='gamma6_sourceid', blank=True, related_name='rn_gamma6_sourceid')
    delta6 = models.FloatField()
    delta6_prec = models.FloatField()
    delta6_sourceid = models.ForeignKey(Sources, null=True, db_column='delta6_sourceid', blank=True, related_name='rn_delta6_sourceid')
    nexp6 = models.FloatField()
    nexp6_prec = models.FloatField()
    nexp6_sourceid = models.ForeignKey(Sources, null=True, db_column='nexp6_sourceid', blank=True, related_name='rn_nexp6_sourceid')
    gamma7 = models.FloatField()
    gamma7_prec = models.FloatField()
    gamma7_sourceid = models.ForeignKey(Sources, null=True, db_column='gamma7_sourceid', blank=True, related_name='rn_gamma7_sourceid')
    delta7 = models.FloatField()
    delta7_prec = models.FloatField()
    delta7_sourceid = models.ForeignKey(Sources, null=True, db_column='delta7_sourceid', blank=True, related_name='rn_delta7_sourceid')
    nexp7 = models.FloatField()
    nexp7_prec = models.FloatField()
    nexp7_sourceid = models.ForeignKey(Sources, null=True, db_column='nexp7_sourceid', blank=True, related_name='rn_nexp7_sourceid')
    gamma8 = models.FloatField()
    gamma8_prec = models.FloatField()
    gamma8_sourceid = models.ForeignKey(Sources, null=True, db_column='gamma8_sourceid', blank=True, related_name='rn_gamma8_sourceid')
    delta8 = models.FloatField()
    delta8_prec = models.FloatField()
    delta8_sourceid = models.ForeignKey(Sources, null=True, db_column='delta8_sourceid', blank=True, related_name='rn_delta8_sourceid')
    nexp8 = models.FloatField()
    nexp8_prec = models.FloatField()
    nexp8_sourceid = models.ForeignKey(Sources, null=True, db_column='nexp8_sourceid', blank=True, related_name='rn_nexp8_sourceid')
    gamma9 = models.FloatField()
    gamma9_prec = models.FloatField()
    gamma9_sourceid = models.ForeignKey(Sources, null=True, db_column='gamma9_sourceid', blank=True, related_name='rn_gamma9_sourceid')
    delta9 = models.FloatField()
    delta9_prec = models.FloatField()
    delta9_sourceid = models.ForeignKey(Sources, null=True, db_column='delta9_sourceid', blank=True, related_name='rn_delta9_sourceid')
    nexp9 = models.FloatField()
    nexp9_prec = models.FloatField()
    nexp9_sourceid = models.ForeignKey(Sources, null=True, db_column='nexp9_sourceid', blank=True, related_name='rn_nexp9_sourceid')
    class Meta:
        db_table = u'transitions'

