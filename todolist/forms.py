from django import forms
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

class FormTodo(forms.ModelForm):
    class Meta():
        model = models.TodoItem
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(),
        }


class FormTodoDelete(forms.ModelForm):
    class Meta():
        model = models.TodoItem
        fields = []

