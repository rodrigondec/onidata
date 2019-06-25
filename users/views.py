from rest_framework import viewsets

from users.serializers import (
    UserCreateSerializer, UserListSerializer, UserUpdateSerializer,
    User)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    authentication_classes = []
    permission_classes = []

    def get_serializer_class(self):
        update_actions = (
            'update',
            'partial_update',
        )

        if self.action == 'create':
            return UserCreateSerializer
        elif self.action in update_actions:
            return UserUpdateSerializer
        return self.serializer_class
