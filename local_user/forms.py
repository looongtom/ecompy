from django import forms
from .models import LocalUser

class LocalUserForm(forms.ModelForm):
    class Meta:
        model = LocalUser
        fields = ['full_name', 'email', 'password', 'phone', 'address']  # Add other fields as needed