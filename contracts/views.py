from rest_framework import viewsets

from contracts.serializers import ContractSerializer, Contract


class ContractViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows contracts to be viewed or edited.
    """
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    authentication_classes = []
    permission_classes = []
