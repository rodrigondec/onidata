from unittest.mock import patch, MagicMock

from django.test import TestCase

from core.permissions import IsOwner


class IsOwnerTestCase(TestCase):
    def setUp(self):
        self.permission = IsOwner()
        self.view = MagicMock()

    def test_owner(self):
        request = MagicMock(user=MagicMock())
        obj = MagicMock(owner=request.user)

        self.assertTrue(self.permission.has_object_permission(request, self.view, obj))

    def test_not_owner(self):
        request = MagicMock(user=MagicMock())
        obj = MagicMock(owner=MagicMock())

        self.assertFalse(self.permission.has_object_permission(request, self.view, obj))
