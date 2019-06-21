from rest_framework import viewsets

from users.serializers import UserSerializer, User


class UserViewSet(viewsets.ModelViewSet):
    """
        A generic Viewset for Users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []
