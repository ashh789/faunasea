from django import forms
from django.forms import ModelForm
from . models import commentbox

class commentboxForm(ModelForm):
    class Meta:
        model=commentbox
        fields=['box']
