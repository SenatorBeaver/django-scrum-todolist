from django import forms
from django.forms import DateInput, TimeInput

from . import models

class TodoitemForm(forms.ModelForm):
    class Meta:
        model = models.TodoItem
        fields = ('text', 'priority', 'project')
        widgets = {
            'due_date': DateInput,
            'due_time': TimeInput,
        }

class TodoitemTimeForm(forms.ModelForm):
    class Meta:
        model = models.TodoItem
        fields = ('period_type', 'period_value', 'due_date', 'due_time')
        widgets = {
            'due_date': DateInput,
            'due_time' : TimeInput,
        }

