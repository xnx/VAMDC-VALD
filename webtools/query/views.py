# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django import forms
from django.forms.formsets import formset_factory

from models import Query
import registry

try: REGISTRY = registry.getNodeList()
except: REGISTRY = [{'name':'Registry is down','url':None}]

import string as s
from random import choice
def makeQID(length=6, chars=s.letters + s.digits):
    return ''.join([choice(chars) for i in xrange(length)])

from urllib import urlopen,urlencode

PARA_CHOICES=[('',u'----'),
              ('AtomSymbol',u'Atom Name'),
              ('AtomNuclearCharge',u'Atomic number'),
              ('AtomIonCharge',u'Ionization state (0=neutral)'),
              ('AtomStateEnergy',u'Atomic state energy (eV)'),
              ('',u'----'),
              ('RadTransWavelengthExperimentalValue',u'(Radiative transition) Wavelength (Å)'),
              ('RadTransProbabilityLog10WeightedOscillatorStrengthValue',u'(Radiative transition) Oscillator strength, log(g*f)'),
              ('',u'----'),
              ('MolecularSpeciesChemicalName',u'Molecule Name'),
              ('MolecularStateEnergyValue',u'Molecular Sate Energy'),
#              ('',u'Species from species list (not implemented)'),
]

class ConditionForm(forms.Form):
    lower=forms.CharField(max_length=8,required=False,initial=None,label='lower bound',widget=forms.widgets.TextInput(attrs={'size':'8'}))
    parameter=forms.ChoiceField(label='parameter to restrict',required=True,initial='',choices=PARA_CHOICES)
    upper=forms.CharField(max_length=8,required=False,initial=None,label='upper bound',widget=forms.widgets.TextInput(attrs={'size':'8'}))
    connection=forms.BooleanField(initial=True,required=False,label='Use AND to connect with next condition?')
    
    def validate(self,value):
        # check here e.g. if the lower bound <= upper
        super(ConditionForm,self).validate(value)              

def constructQuery(constraints):
    q='select all where '
    for c in constraints:
        if c == {}: continue
        if not c['parameter']: continue
        if c['lower'] and c['upper']:
            if c['lower'] == c['upper']: q+='( %s = %s )'%(c['parameter'],c['upper'])
            else:
                q+='( %s > %s and '%(c['parameter'],c['lower'])
                q+='%s < %s )'%(c['parameter'],c['upper'])
        elif c['lower']:
            q+='( %s > %s )'%(c['parameter'],c['lower'])
        elif c['upper']:
            q+='( %s < %s )'%(c['parameter'],c['upper'])
        else:
            q+='( %s notnull )'%c['parameter']

        if c['connection']: q+=' AND '
        else: q+=' OR  '
    return q[:-5] # remove the last AND/OR

def query(request):
    ConditionSet = formset_factory(ConditionForm, extra=5)
    if request.method == 'POST':
        selectionset = ConditionSet(request.POST,request.FILES) 
        if selectionset.is_valid():
            query=Query(qid=makeQID(),query=constructQuery(selectionset.cleaned_data))
            query.save()
            return HttpResponseRedirect('/portal/results/%s/'%query.qid) 
    else:
        selectionset = ConditionSet(initial=[
                {'lower': u'5000',
                 'upper': u'5050',
                 'parameter':'RadTransWavelengthExperimentalValue',
                 'connection':True,
                 },
                ])
        
    return render_to_response('portal/query.html', {'selectionset': selectionset})


def index(request):
    c=RequestContext(request,{})
    return render_to_response('portal/index.html', c)



#####################

def makeDlLink(url,query,format='XSAMS'):
    data={}
    data['LANG']='VSS1'
    data['QUERY']=query
    data['FORMAT']=format
    data=urlencode(data)
    return url+'sync?'+data
    
def results(request,qid):
    query=Query.objects.get(pk=qid)
    results=[]
    for node in REGISTRY:
        result={'nodename':node['name']}
        if node['url']:
	    result['xsamsurl']=makeDlLink(node['url'],query.query)
	else: result['xsamsurl']=None
        results.append(result)
        
    return render_to_response('portal/results.html', {'results': results, 
                                                      'query':query,
                                                      })



######################
class SQLqueryForm(forms.Form):
    sql=forms.CharField(label='Enter your SQL query',widget=forms.widgets.Textarea(attrs={'cols':'40','rows':'5'}),required=True)


def sqlquery(request):
    if request.method == 'POST':
        form = SQLqueryForm(request.POST) 
        if form.is_valid():
            #print form.cleaned_data
            pass

    else:
        form=SQLqueryForm()
        
    return render_to_response('portal/sqlquery.html', {'form': form})

