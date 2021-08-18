from rest_framework import serializers

from .backends import UserAuthBackend, authenticate

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'login')

    def create(self, validated_data):
        user = User.objects.create_user(
            **validated_data
        )
        return user


class LoginSerializer(serializers.Serializer):
    def validate(self, data):
        user = authenticate()
        if user:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
