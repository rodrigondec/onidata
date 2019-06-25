from rest_framework import serializers

from users.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username', 'first_name', 'last_name']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class PasswordResetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'password']
        extra_kwargs = {
            'id': {'read_only': True},
        }
