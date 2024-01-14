from django import forms
from .models import Task

class YourForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['image', 'title', 'task']  