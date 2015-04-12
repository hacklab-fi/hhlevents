# -*- coding: UTF-8 -*-
from django import forms


class RegForm(forms.Form):
    first_name = forms.CharField(max_length=150, required=True, label=u'Etunimi')
    last_name = forms.CharField(max_length=150, required=True, label=u'Sukunimi')
    email = forms.EmailField(required=True, label=u'E-Mail')
    email2 = forms.EmailField(required=True, label='E-Mail (uudelleen)', help_text=u'Hoidamme kaiken mailitse, osoitteen on oltava oikein')

    wants_materials = forms.BooleanField(label=u'Haluan materiaalipaketin')

    # If the person wants to join HHL
    join = forms.BooleanField(label=u'Haluan liittyä jäseneksi')
    city = forms.CharField(max_length=150, label)=u'Paikkakunta')
    

    def clean(self, *args, **kwargs):
        email = self.cleaned_data['email']
        email2 = self.cleaned_data['email2']
        if email != email2:
            raise forms.ValidationError(u'E-Mail osoitteet eivät täsmää')
        return self.cleaned_data
