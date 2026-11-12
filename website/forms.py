from django import forms
from .models import ProjectRequest

class ProjectRequestForm(forms.ModelForm):
    class Meta:
        model = ProjectRequest
        fields = ['name', 'company', 'email', 'phone', 'domain', 'location', 'description', 'budget', 'timeline', 'document']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }
