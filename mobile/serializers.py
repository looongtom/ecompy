from unicodedata import name
from rest_framework import serializers

from .models import Mobile

class MobileSerializer(serializers.ModelSerializer):
    name = serializers.CharField( max_length=255)
    brand = serializers.CharField( max_length=255)
    price = serializers.IntegerField()
    description = serializers.CharField( max_length=255)
    image = serializers.ImageField(
        max_length=None,
        use_url=True
    ) 
    class Meta:  
        model = Mobile
        fields = ('id','image','name', 'brand', 'price', 'description')