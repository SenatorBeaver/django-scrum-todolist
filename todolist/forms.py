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

