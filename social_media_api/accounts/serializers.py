from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError("Both email and password are required.")

        # Try to authenticate using username/email
        user = authenticate(username=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid credentials.")

        data['user'] = user
        return data


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField()   
    last_name = serializers.CharField()   
    email = serializers.CharField(max_length=255)        
    password = serializers.CharField(max_length=128, write_only=True)  

    def create(self, validated_data):
        # Create user with hashed password
        user = get_user_model().objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            username=validated_data['email'],
            password=validated_data['password']
        )

        # Create a DRF token for the new user
        Token.objects.create(user=user)

        return user
