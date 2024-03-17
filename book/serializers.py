from rest_framework import serializers

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    name = serializers.CharField( max_length=255)
    author = serializers.CharField( max_length=255)
    price = serializers.IntegerField()
    description = serializers.CharField( max_length=255)
    image = serializers.ImageField(
        max_length=None,
        use_url=True
    )
    class Meta:  
        model = Book
        fields = ('id','image','name', 'author', 'price', 'description')