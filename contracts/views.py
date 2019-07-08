from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status

from core.permissions import IsAuthenticatedOrCreate, IsOwnerOrAdmin
from contracts.serializers import ContractSerializer, Contract
from core.utils import get_client_ip


class ContractViewSet(ModelViewSet):
    """
    API endpoint that allows contracts to be viewed or edited.
    """
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticatedOrCreate, IsOwnerOrAdmin]

    def list(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            self.queryset = self.queryset.filter(client=request.user)
        return super(ContractViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.queryset.create(ip_address=get_client_ip(request), **serializer.validated_data)
        headers = self.get_success_headers(serializer.data)
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
