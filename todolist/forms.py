from django import forms
from django.forms import DateTimeInput

from . import models

class TodoitemForm(forms.ModelForm):
    class Meta:
        model = models.TodoItem
        fields = ('text', 'priority', 'project')
        widgets = {
            'due_date': DateTimeInput
        }

class TodoitemTimeForm(forms.ModelForm):
    class Meta:
        model = models.TodoItem
        fields = ('period_value', 'period_type', 'due_date')
        widgets = {
            'due_date': DateTimeInput
        }

    def __init__(self, *args, **kwargs):
        super(TodoitemTimeForm, self).__init__(*args, **kwargs)
        self.fields['due_date'].required = False
