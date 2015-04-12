# -*- coding: UTF-8 -*-
from django import forms


class RegForm(forms.Form):
    first_name = forms.CharField(max_length=150, required=True, label=u'Etunimi')
    last_name = forms.CharField(max_length=150, required=True, label=u'Sukunimi')
    email = forms.EmailField(required=True, label=u'E-Mail')
    email2 = forms.EmailField(required=True, label='E-Mail (uudelleen)', help_text=u'Hoidamme kaiken mailitse, osoitteen on oltava oikein')

    wants_materials = forms.BooleanField(label=u'Haluan materiaalipaketin', required=False)

    # If the person wants to join HHL
    join = forms.BooleanField(label=u'Haluan liittyä jäseneksi', required=False)
    city = forms.CharField(max_length=150, label=u'Paikkakunta', required=False)
    

    def clean(self, *args, **kwargs):
        cleaned_data = super(RegForm, self).clean()
        email = cleaned_data.get('email', None)
        email2 = cleaned_data.get('email2', None)
        if email != email2:
            self.add_error('email2', u'E-Mail osoitteet eivät täsmää')

        if cleaned_data.get('join', None):
            if not cleaned_data.get('city', None):
                self.add_error('city', u'Jäseneksi liittyviltä vaaditaan paikkakunta')
        return cleaned_data
