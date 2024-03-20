from django import forms
from .models import Shipment

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = Shipment
        fields = ['user_id','order_id','address','date','status']  # Add other fields as needed