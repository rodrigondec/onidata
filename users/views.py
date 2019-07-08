from rest_framework.viewsets import ModelViewSet

from core.permissions import IsAuthenticatedOrCreate, IsOwner
from users.serializers import (
    UserCreateSerializer, UserListSerializer, UserUpdateSerializer,
    User)


class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticatedOrCreate, IsOwner]

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
