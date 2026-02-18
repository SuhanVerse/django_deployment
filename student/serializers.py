from rest_framework import serializers
from django.contrib.auth.hashers import make_password
# from django.utils import timezone
from .models import Registration

class RegistrationSerializer(serializers.Serializer):
    """Registration serializer with comprehensive validation"""

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        max_length=100,
        error_messages={'required': 'Name is required', 'blank': 'Name is required'}
    )
    email = serializers.EmailField(
        error_messages={'required': 'Email is required', 'invalid': 'Enter a valid email address'}
    )
    password = serializers.CharField(
        write_only=True,
        error_messages={'required': 'Password is required', 'blank': 'Password is required'}
    )
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return Registration.objects.create(**validated_data)
    
    def validate_password(self, value):
        """Password must be more than 8 characters"""
        if len(value) <= 8:
            raise serializers.ValidationError(
                'Password must be more than 8 characters'
            )
        return value