from django import forms
from teachers.models import Teachers

class TeachersForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = ('f_name','s_name')
