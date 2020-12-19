from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """
    class Meta:
        model = get_user_model()
        fields = ('name', 'email', 'password', 'user_type')
        extra_kwargs = {
            'password': {
                'write_only': True, 'min_length': 5
            }
        }
        
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for User authentication.
    """
    email = serializers.EmailField(max_length=254)
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )

        if not user:
            msg = _('Invalid Email or Password')
            raise serializers.ValidationError(msg, code='authentication')
        attrs['user'] = user
        return attrs