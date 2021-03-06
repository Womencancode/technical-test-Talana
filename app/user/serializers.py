from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from user.models import Request
from car.models import Car


# ____________________User objects serializers____________________

class UserListSerializer(serializers.ModelSerializer):
    """Serializes a user object for listing them all"""
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'email',
            'name'
        )


class UserPostSerializer(serializers.ModelSerializer):
    """Serializes a user object for post, put and patch methods"""

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'email',
            'password',
            'name',
            'last_name',
            'telephone'

        )
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                },
                'min_length': 6,
            }
        }

    def create(self, validated_data):
        """Create and  return  new user"""
        user = get_user_model().objects.create_user(**validated_data)
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    """Serializes a user object for post, put and patch methods"""

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'email',
            'password',
            'name',
            'last_name',
            'telephone'

        )
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                },
                'min_length': 6,
            }
        }

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)  # remove the password
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    """Serializes a user object"""

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'name',
            'last_name',
            'email',
            'telephone',
            'is_available'

        )


# ____________________Auth-token objects serializers____________________

class AuthTokenSerializer(serializers.Serializer):
    """Serializer for  user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate user"""
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )

        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return attrs


# ____________________Request objects serializers____________________

class RequestListSerializer(serializers.ModelSerializer):
    """Serializes a Request object"""
    user = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all()
    )
    car = serializers.PrimaryKeyRelatedField(
        queryset=Car.objects.all()
    )
    state = serializers.CharField(source='get_state_display')

    class Meta:
        model = Request
        fields = (
            'id',
            'user',
            'car',
            'state'
        )


class RequestSerializer(serializers.ModelSerializer):
    """Serializes a construction company object"""
    user = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all()
    )
    car = serializers.PrimaryKeyRelatedField(
        queryset=Car.objects.all()
    )

    class Meta:
        model = Request
        fields = (
            'id',
            'user',
            'car',
            'retirement_date',
            'return_date',
            'state'
        )

    def create(self, validated_data):
        """Create and  return  new Request"""
        request = Request.objects.create(**validated_data)
        return request

    def update(self, instance, validated_data):
        """Update a Request object and return it"""
        request = super().update(instance, validated_data)
        return request


class RequestDetailSerializer(serializers.ModelSerializer):
    """Serializes a Request object"""
    state = serializers.CharField(source='get_state_display')

    class Meta:
        model = Request
        fields = '__all__'
