from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.permissions import IsOwner
from payments.serializers import PaymentSerializer, Payment


class PaymentViewSet(ModelViewSet):
    """
    API endpoint that allows payments to be viewed or edited.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(contract__client=request.user)
        return super(PaymentViewSet, self).list(request, *args, **kwargs)
