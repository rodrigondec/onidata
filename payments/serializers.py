from rest_framework import serializers

from core.serializer_fields import UUIDRelatedField
from payments.models import Payment
from contracts.models import Contract


class PaymentSerializer(serializers.ModelSerializer):
    contract_id = UUIDRelatedField(Contract, help_text='Contrato do pagamento')

    class Meta:
        model = Payment
        fields = ['id', 'contract_id', 'value']
        extra_kwargs = {
            'id': {'read_only': True}
        }
