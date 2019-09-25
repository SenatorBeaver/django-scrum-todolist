from django import forms
from django.forms import DateInput

from . import models

class TodoitemForm(forms.ModelForm):
    class Meta:
        model = models.TodoItem
        fields = ('text', 'priority', 'project')
        widgets = {
            'due_date': DateInput
        }

class TodoitemTimeForm(forms.ModelForm):
    class Meta:
        model = models.TodoItem
        fields = ('period_type', 'period_value', 'due_date')
        widgets = {
            'due_date': DateInput
        }

    def __init__(self, *args, **kwargs):
        super(TodoitemTimeForm, self).__init__(*args, **kwargs)
        self.fields['due_date'].required = False
