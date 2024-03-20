from rest_framework import serializers

from .models import Payment_Order

class Payment_OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Order
        fields = '__all__'
