from rest_framework.viewsets import ModelViewSet

from core.permissions import IsAuthenticatedOrCreate, IsOwnerOrCreate
from payments.serializers import PaymentSerializer, Payment


class PaymentViewSet(ModelViewSet):
    """
    API endpoint that allows payments to be viewed or edited.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticatedOrCreate, IsOwnerOrCreate]
