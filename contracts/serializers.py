from rest_framework import serializers

from core.serializer_fields import ModelField
from contracts.models import Contract
from users.models import User


class ContractSerializer(serializers.ModelSerializer):
    user = ModelField(User, help_text='Usuário do contrato')

    class Meta:
        model = Contract
        fields = ['id', 'user', 'info']
        extra_kwargs = {
            'id': {'read_only': True}
        }
