from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView

from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404

from . models import User
from . serializers import UserCreateSerializer, UserLoginSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(CreateAPIView):
    
    def get_serializer_class(self):
        return UserCreateSerializer

    def post(self, request, format=None):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token':token}, status=status.HTTP_201_CREATED)
    

class UserLoginView(CreateAPIView):
 
  def get_serializer_class(self):
      return UserLoginSerializer

  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.data.get('username')
    password = serializer.data.get('password')

    print(username, password)

    user = authenticate(username=username, password=password)

    print(user, "hello")
    
    if user is not None:
        token = get_tokens_for_user(user)
        return Response({'token':token}, status=status.HTTP_200_OK)
    else:
        Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)