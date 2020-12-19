from django.shortcuts import render

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import OrderSerializer
from .models import Order

# Create your views here.

class OrderView(ListCreateAPIView):
    """
    This view allows sellers (user_type: 'S') to list all the orders belonging
    to them. Also allows buyers (user_type: 'B') to place an order.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        if request.user.user_type == 'B':
            return super().create(request, *args, **kwargs)
        return Response('Not Allowed', status=status.HTTP_401_UNAUTHORIZED)

    def perform_create(self, serializer):
        serializer.save(buyer = self.request.user)
    
    def list(self, request, *args, **kwargs):
        if request.user.user_type == 'S':
            queryset = self.queryset.filter(plant__seller=request.user)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        return Response('Not Allowed', status=status.HTTP_401_UNAUTHORIZED)