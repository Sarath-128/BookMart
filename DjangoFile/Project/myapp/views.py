from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from django.contrib import auth

# User Details

class UserCreate(generics.ListCreateAPIView):  
    queryset=User.objects.all()
    serializer_class= UserSerializer
    permission_classes=[AllowAny]

class UserUpdate(generics.UpdateAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializer

class UserDetails(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializer

class UserDelete(generics.DestroyAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializer

# Book Details

class BookCreate(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class= BookSerializer
    permission_classes=[AllowAny]

class Bookupdate(generics.UpdateAPIView):
    queryset=Book.objects.all()
    serializer_class= BookSerializer

class BookDetails(generics.RetrieveAPIView):
    queryset=Book.objects.all()
    serializer_class= BookSerializer

class BookDelete(generics.DestroyAPIView):
    queryset=Book.objects.all()
    serializer_class= BookSerializer
  
# Admin Register
  
class Register(generics.ListCreateAPIView):
    queryset=AdminDetails.objects.all()
    serializer_class= RegisterSerializer
    permission_classes=[AllowAny]

class RegisterDelete(generics.DestroyAPIView):
    queryset=AdminDetails.objects.all()
    serializer_class= RegisterSerializer

# Admin Login

class Login(generics.ListAPIView):
    queryset = AdminDetails.objects.all()
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')  # Use request.data for POST requests
        password = request.data.get('password', '')

        users = AdminDetails.objects.filter(username=username, password=password)

        if users.exists():
            print("success")
            user = users.first()  # Retrieve the first user from the queryset
            serializer = self.serializer_class(user)  # Use the serializer class directly
            return Response({'message': 'Login Successful', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            print("faild")
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)