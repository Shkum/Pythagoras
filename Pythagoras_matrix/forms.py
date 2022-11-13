from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class UserData(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'date']
        widgets = {
            'date': DateInput(attrs={'type': 'date'}),
        }
        # exclude = ['']
