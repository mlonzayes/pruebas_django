from django import forms
from .models import Project

class CreateNewTask(forms.Form):
    title=forms.CharField(max_length=200)
    description=forms.CharField(widget=forms.Textarea,label="Descrption",required=True)
    project_id=forms.ModelChoiceField(queryset=Project.objects.all())

class CreateNewProject(forms.Form):
    name=forms.CharField(max_length=200)