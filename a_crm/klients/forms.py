from django import forms
from klients.models import Klients

class KlientForm(forms.ModelForm):
    class Meta:
        model = Klients
        fields = ('f_name','s_name','servise','town','school','status','istochnik')

