from django import forms


class RegForm(forms.Form):
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    email2 = forms.EmailField(required=True)

    wants_materials = forms.BooleanField()

    # If the person is member
    is_member = forms.BooleanField()

    # If the person wants to join HHL
    join = forms.BooleanField()
    city = forms.CharField(max_length=150)
    

    def clean(self, *args, **kwargs):
        email = self.cleaned_data['email']
        email2 = self.cleaned_data['email2']
        if email != email2:
            raise forms.ValidationError("Emails don't match")
        return self.cleaned_data
