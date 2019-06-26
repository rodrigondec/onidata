from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework_extensions.mixins import NestedViewSetMixin

from contracts.serializers import ContractSerializer, Contract


class ContractReadViewSet(NestedViewSetMixin, GenericViewSet, ListModelMixin, RetrieveModelMixin):
    """
    API endpoint that allows contracts to be viewed.
    """
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    authentication_classes = []
    permission_classes = []


class ContractViewSet(ModelViewSet):
    """
    API endpoint that allows contracts to be viewed or edited.
    """
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    authentication_classes = []
    permission_classes = []
