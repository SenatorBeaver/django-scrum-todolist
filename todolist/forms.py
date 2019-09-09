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


class FormDocPrefix(forms.ModelForm):
    class Meta():
        model = models.DocPrefix
        fields = '__all__'


class FormDocPrefixDelete(forms.ModelForm):
    class Meta():
        model = models.DocPrefix
        fields = []


class FormDocRevision(forms.ModelForm):
    class Meta():
        model = models.Document
        exclude = ['doc_prefix_id']


class FormDocRevisionDelete(forms.ModelForm):
    class Meta():
        model = models.Document
        fields = []
