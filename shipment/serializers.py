from rest_framework import serializers
from .models import Shipment

class ShipmentSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    order_id = serializers.IntegerField()
    address = serializers.CharField(max_length=255)
    date = serializers.DateTimeField()
    status = serializers.CharField(max_length=255)
    class Meta:  
        model = Shipment
        fields = ('id','user_id','order_id','address','date','status')