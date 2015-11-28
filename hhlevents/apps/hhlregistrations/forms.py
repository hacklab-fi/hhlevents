# -*- coding: UTF-8 -*-
from django import forms


class RegForm(forms.Form):
    first_name = forms.CharField(max_length=150, required=True, label=u'Etunimi')
    last_name = forms.CharField(max_length=150, required=True, label=u'Sukunimi')
    email = forms.EmailField(required=True, label=u'E-Mail')

    wants_materials = forms.BooleanField(label=u'Haluan materiaalipaketin', required=False)

    # If the person wants to join the organization
    #join = forms.BooleanField(label=u'Haluan liittyä jäseneksi', required=False)
    #city = forms.CharField(max_length=150, label=u'Paikkakunta', required=False)
    
    
    def clean(self, *args, **kwargs):
        cleaned_data = super(RegForm, self).clean()
 
         # TODO: Check for double registrations

        #if cleaned_data.get('join', None):
        #    if not cleaned_data.get('city', None):
        #        self.add_error('city', u'Jäseneksi liittyviltä vaaditaan paikkakunta')

        
        self.cleaned_data = cleaned_data
        return self.cleaned_data
        
