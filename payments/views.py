from rest_framework.viewsets import ModelViewSet

from core.permissions import IsAuthenticatedOrCreate, IsOwner
from payments.serializers import PaymentSerializer, Payment


class PaymentViewSet(ModelViewSet):
    """
    API endpoint that allows payments to be viewed or edited.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticatedOrCreate, IsOwner]

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(contract__client=request.user)
        return super(PaymentViewSet, self).list(request, *args, **kwargs)
