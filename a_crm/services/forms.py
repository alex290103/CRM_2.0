from django import forms
from services.models import Servise

class ServiseForm(forms.ModelForm):
    #teacher = forms.ModelChoiceField(queryset=None)
    class Meta:
        model = Servise
        fields = ('name','type','teacher')
