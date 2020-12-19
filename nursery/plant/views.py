from django.shortcuts import render

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.mixins import CreateModelMixin, ListModelMixin, \
    RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Plant
from .serializers import PlantSerializer

# Create your views here.

class PlantView(GenericViewSet, CreateModelMixin, ListModelMixin, \
    RetrieveModelMixin):
    """
    This view allows sellers (user_type: 'S') to add a plant. Also allows
    buyers (user_type: 'B') to list all plants as well as view a plant.
    """
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        if request.user.user_type == 'S':
            return super().create(request, *args, **kwargs)
        return Response('Not Allowed', status=status.HTTP_401_UNAUTHORIZED)
    
    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)
    
    def list(self, request, *args, **kwargs):
        if request.user.user_type == 'B':
            serializer = PlantSerializer(self.queryset, many=True)
            return Response(serializer.data)
        return Response('Not Allowed', status=status.HTTP_401_UNAUTHORIZED)
    
    def retrieve(self, request, *args, **kwargs):
        if request.user.user_type == 'B':
            return super().retrieve(request, *args, **kwargs)
        return Response('Not Allowed', status=status.HTTP_401_UNAUTHORIZED)