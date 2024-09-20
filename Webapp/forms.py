from django import forms
from Webapp.models import TrainerRequest


class TrainerRequestForm(forms.ModelForm):
    class Meta:
        model = TrainerRequest
        fields = ('name', 'email', 'phone', 'course', 'experience', 'certification', 'image')
