from django import forms
from tasks.models import Tasks
from django.forms.widgets import DateInput

class TaskForm(forms.ModelForm):
    task = forms.CharField(max_length=50, label='Задача')
    class Meta:
        model = Tasks
        fields = ('task','klient','deadline','teacher',)
        widgets = {
            'deadline': DateInput(attrs={'placeholder': 'dd.mm.yyyy'}),
        }

