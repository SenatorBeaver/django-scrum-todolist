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

    def __init__(self, *args, **kwargs):
        super(FormTodo, self).__init__(*args, **kwargs)
        self.fields['label_id'].required = False


class FormTodoDelete(forms.ModelForm):
    class Meta():
        model = models.TodoItem
        fields = []

