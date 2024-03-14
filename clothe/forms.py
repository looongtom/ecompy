from django import forms
from .models import Clothe

class ClotheForm(forms.ModelForm):
    class Meta:
        model = Clothe
        fields = ['name','image' ,'brand','price','description']  # Add other fields as needed