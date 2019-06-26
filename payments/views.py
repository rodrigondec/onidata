from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework_extensions.mixins import NestedViewSetMixin

from payments.serializers import PaymentSerializer, Payment


class PaymentReadViewSet(NestedViewSetMixin, GenericViewSet, ListModelMixin, RetrieveModelMixin):
    """
    API endpoint that allows payments to be viewed.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    authentication_classes = []
    permission_classes = []


class PaymentViewSet(ModelViewSet):
    """
    API endpoint that allows payments to be viewed or edited.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    authentication_classes = []
    permission_classes = []
