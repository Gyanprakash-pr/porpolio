from django import forms
from .models import Project, Resume

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'resume_file']  # Sirf zaroori fields ko include kiya hai
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'resume_file': forms.FileInput(attrs={'class': 'form-control'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'github_link']