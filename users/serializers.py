from rest_framework import serializers

from users.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username', 'first_name', 'last_name']
        extra_kwargs = {
            'id': {'read_only': True},
        }

    def create(self, validated_data):
        user = super(UserCreateSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


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
            'password': {'write_only': True}
        }

    def update(self, instance, validated_data):
        assert isinstance(instance, User)
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance
