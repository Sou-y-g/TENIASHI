from dataclasses import field
from django import forms
from .models import project

class ProjectFrom(forms.ModelForm):
    class Meta:        
        model = project
        fields = '__all__'
        