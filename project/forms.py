from django.forms import ModelForm, fields
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model=Project
        #fields='__all__'
        fields=['title','featured_image', 'description','demo_link','source_link','tags']