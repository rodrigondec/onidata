from rest_framework import serializers

from core.serializer_fields import UUIDRelatedField
from contracts.models import Contract
from users.models import User


class ContractSerializer(serializers.ModelSerializer):
    client_id = UUIDRelatedField(User, help_text='Usuário do contrato')

    class Meta:
        model = Contract
        fields = ['id', 'client_id', 'bank',
                  'amount', 'interest_rate', 'submission_date',
                  'updated_value', 'amount_due', 'ip_address']
        extra_kwargs = {
            'id': {'read_only': True},
            'ip_address': {'required': False},
            'updated_value': {'read_only': True},
            'amount_due': {'read_only': True}
        }
