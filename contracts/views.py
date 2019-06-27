from rest_framework.viewsets import ModelViewSet

from core.permissions import IsAuthenticatedOrCreate, IsOwnerOrCreate
from contracts.serializers import ContractSerializer, Contract


class ContractViewSet(ModelViewSet):
    """
    API endpoint that allows contracts to be viewed or edited.
    """
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticatedOrCreate, IsOwnerOrCreate]

