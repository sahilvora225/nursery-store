from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken

from .serializers import UserSerializer, UserLoginSerializer

# Create your views here.

class CreateUserView(CreateAPIView):
    """
    A view to create User object or Sing Up.
    """
    serializer_class = UserSerializer


class LoginView(ObtainAuthToken):
    """
    A view for user to login.
    """
    serializer_class = UserLoginSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES