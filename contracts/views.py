from rest_framework.viewsets import ModelViewSet

from core.permissions import IsAuthenticatedOrCreate, IsOwnerOrCreate
from contracts.serializers import ContractSerializer, Contract
from core.utils import get_client_ip


class ContractViewSet(ModelViewSet):
    """
    API endpoint that allows contracts to be viewed or edited.
    """
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticatedOrCreate, IsOwnerOrCreate]

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(client=request.user)
        return super(ContractViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        request.data['ip_address'] = get_client_ip(request)
        return super(ContractViewSet, self).create(request, *args, **kwargs)
