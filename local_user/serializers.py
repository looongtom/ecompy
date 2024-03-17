from rest_framework import serializers
from .models import (
    User
)
import re

class UserJson(serializers.ModelSerializer):
    re_password = serializers.CharField(write_only=True)
    role = serializers.CharField(max_length=30, required=False)
    password = serializers.CharField(max_length=18, required=False)
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 're_password', 'phone', 'address', 'role', 'full_name']

    def create(self, validated_data):
        validated_data.pop('re_password')  # Loại bỏ trường re_password khi tạo mới User
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('re_password')  # Loại bỏ trường re_password khi cập nhật User
        return super().update(instance, validated_data)

    
    def validate_id(self, value):
        request_method = self.context['request'].method

        if value is None and request_method == 'PUT':
            raise serializers.ValidationError("Id must not be empty")
        return value
    
    def validate_email(self, value):
        request_method = self.context['request'].method

        if value is None and request_method == 'PUT':
            self.initial_data.pop('email', None)
            return
        
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value):
            raise serializers.ValidationError("Email not in format")
        return value
    
    def validate_password(self, value):
        request_method = self.context['request'].method

        if value is None and request_method == 'PUT':
            self.initial_data.pop('password', None)
            return
        
        if len(value) < 8 or len(value) > 16:
            raise serializers.ValidationError("Length of password must between 8 and 16")
        return value
    
    def validate_re_password(self, value):
        request_method = self.context['request'].method

        if value is None and request_method == 'PUT'         :
            self.initial_data.pop('re_password', None)
            return
        
        if len(value) < 8 or len(value) > 16:
            raise serializers.ValidationError("Length of re_password must between 8 and 16")
        
        password = self.initial_data.get('password')
        if value != password:
            raise serializers.ValidationError("Passwords do not match")
        return value
    
    def validate_phone(self, value):
        request_method = self.context['request'].method

        if value is None and request_method == 'PUT'         :
            self.initial_data.pop('phone', None)
            return
        
        if not re.match(r'^0\d{1,8}$', value):
            raise serializers.ValidationError("Phone's lenth must be 9 and start by '0'")
        return value
    
    def validate_address(self, value):
        request_method = self.context['request'].method

        if value is None and request_method == 'PUT'         :
            self.initial_data.pop('address', None)
            return
        
        if not re.match(r'^[^\d]+$', value):
            raise serializers.ValidationError("Addresses are not allowed to contain special characters")
        return value
    
    def validate_full_name(self, value):
        request_method = self.context['request'].method

        if value is None and request_method == 'PUT'         :
            self.initial_data.pop('full_name', None)
            return
        
        if not re.match(r'^[^\d]+$', value):
            raise serializers.ValidationError("Fullname are not allowed to contain special characters")
        return value