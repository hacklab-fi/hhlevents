# -*- coding: UTF-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _ # Translating labels requires _lazy variant


class RegForm(forms.Form):
    first_name = forms.CharField(max_length=150, required=True, label=_('First name'))
    last_name = forms.CharField(max_length=150, required=True, label=_('Surname'))
    email = forms.EmailField(required=True, label=_('E-Mail'))

    wants_materials = forms.BooleanField(label=_('I want materials package'), required=False)

    # If the person wants to join the organization
    join = forms.BooleanField(label=_('I want to join as a member'), required=False)
    city = forms.CharField(max_length=150, label=_('Municipality'), required=False)
    

    def clean(self, *args, **kwargs):
        cleaned_data = super(RegForm, self).clean()
 
         # TODO: Check for double registrations

        #if cleaned_data.get('join', None):
        #    if not cleaned_data.get('city', None):
        #        self.add_error('city', _('Please state your municipality'))

        
        self.cleaned_data = cleaned_data
        return self.cleaned_data
        
