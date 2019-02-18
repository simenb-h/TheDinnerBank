from django import forms
from .models import *

class DinnerForm(forms.ModelForm):

    class Meta: 
        model = Dinner
        fields = ['title', 'text', 'image']