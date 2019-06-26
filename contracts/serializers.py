from rest_framework import serializers

from core.serializer_fields import UUIDRelatedField
from contracts.models import Contract
from users.models import User


class ContractSerializer(serializers.ModelSerializer):
    user_id = UUIDRelatedField(User, help_text='Usuário do contrato')

    class Meta:
        model = Contract
        fields = ['id', 'user_id', 'info']
        extra_kwargs = {
            'id': {'read_only': True}
        }
