from django import forms
from django.forms import DateTimeInput

from . import models


class FormProject(forms.ModelForm):
    class Meta():
        model = models.Project
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(),
        }


class FormProjectDelete(forms.ModelForm):
    class Meta():
        model = models.Project
        fields = []


class TodoitemForm(forms.ModelForm):
    class Meta:
        model = models.TodoItem
        fields = ('text', 'priority', 'period_value' , 'period_type', 'due_date', 'project')
        widgets = {
            'due_date': DateTimeInput
        }

    def __init__(self, *args, **kwargs):
        super(TodoitemForm, self).__init__(*args, **kwargs)
        self.fields['project'].required = False
        self.fields['due_date'].required = False


class FormTodoDelete(forms.ModelForm):
    class Meta():
        model = models.TodoItem
        fields = []

