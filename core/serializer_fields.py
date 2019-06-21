import uuid

from rest_framework import serializers


class ModelField(serializers.Field):

    def __init__(self, model, *args, **kwargs):
        self.model = model
        super().__init__(*args, **kwargs)

    def to_representation(self, value):
        assert isinstance(value, self.model)
        return str(value.id)

    def to_internal_value(self, data):
        try:
            instance_id = uuid.UUID(data)
        except ValueError:
            raise serializers.ValidationError('UUID inválido')
        try:
            instance = self.model.objects.get(id=instance_id)
            return instance
        except self.model.DoesNotExist:
            raise serializers.ValidationError(f'{self.model.__name__} não existe')