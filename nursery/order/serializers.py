from rest_framework import serializers

from plant.models import Plant

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for Order model.
    """
    buyer = serializers.PrimaryKeyRelatedField(read_only=True)
    plant = serializers.PrimaryKeyRelatedField(queryset=Plant.objects.all())

    class Meta:
        model = Order
        fields = '__all__'
        read_only = ('id', 'status', 'datetime')