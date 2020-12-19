from rest_framework import serializers

from .models import Plant


class PlantSerializer(serializers.ModelSerializer):
    """
    Serializer for Plant model.
    """
    seller = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Plant
        fields = '__all__'
        read_only = ('id',)