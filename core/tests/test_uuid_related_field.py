import uuid
from unittest.mock import MagicMock

from django.test import TestCase
from rest_framework.serializers import ValidationError

from core.serializer_fields import UUIDRelatedField


class UUIDRelatedFieldTestCase(TestCase):
    def setUp(self):
        self.field = UUIDRelatedField(MagicMock())

    def test_to_representation(self):
        data = self.field.to_representation(uuid.uuid4())
        self.assertIsInstance(data, str)

    def test_build_uuid(self):
        data = self.field.build_uuid(str(uuid.uuid4()))
        self.assertIsInstance(data, uuid.UUID)

    def test_build_uuid_validation(self):
        self.assertRaises(ValidationError, self.field.build_uuid, '123')
