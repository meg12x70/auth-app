from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class AppUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = AppUser
        fields = '__all__'

class CreateAppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'
