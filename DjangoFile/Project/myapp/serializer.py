from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminDetails
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminDetails
        fields = ['id','username','password']


# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(required=True)