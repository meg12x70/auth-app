from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied

from .models import *
from .serializers import *

# Create your views here.
class Logout(APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
 
class AppUserRetrieveView(generics.RetrieveAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    lookup_field = 'user'

class AppUserUpdateView(generics.UpdateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = CreateAppUserSerializer

class AppUserUpdateView(generics.UpdateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = CreateAppUserSerializer

class CreateAppUserView(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = CreateAppUserSerializer

class AppUserListView(generics.ListAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
