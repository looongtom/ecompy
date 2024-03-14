from .models import Mobile
from django import forms



class MobileForm(forms.ModelForm):
    class Meta:
        model=Mobile
        fields=['name','image','brand','price','description']  # Add other fields as needed