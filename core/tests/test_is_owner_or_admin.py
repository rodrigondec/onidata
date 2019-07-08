from unittest.mock import patch, MagicMock

from django.test import TestCase

from core.permissions import IsOwnerOrAdmin


class IsOwnerOrAdminTestCase(TestCase):
    def setUp(self):
        self.permission = IsOwnerOrAdmin()

    def test_retrieve_owner(self):
        request = MagicMock(user=MagicMock(is_superuser=False))
        view = MagicMock(action='retrieve')
        obj = MagicMock(owner=request.user)

        self.assertTrue(self.permission.has_object_permission(request, view, obj))

    def test_retrieve_not_owner(self):
        request = MagicMock(user=MagicMock(is_superuser=False))
        view = MagicMock(action='retrieve')
        obj = MagicMock(owner=MagicMock())

        self.assertFalse(self.permission.has_object_permission(request, view, obj))

    def test_retrieve_owner_admin(self):
        request = MagicMock(user=MagicMock(is_superuser=True))
        view = MagicMock(action='retrieve')
        obj = MagicMock(owner=request.user)

        self.assertTrue(self.permission.has_object_permission(request, view, obj))

    def test_retrieve_not_owner_admin(self):
        request = MagicMock(user=MagicMock(is_superuser=True))
        view = MagicMock(action='retrieve')
        obj = MagicMock(owner=MagicMock())

        self.assertTrue(self.permission.has_object_permission(request, view, obj))

    def test_put_owner(self):
        request = MagicMock(user=MagicMock(is_superuser=False))
        view = MagicMock(action='put')
        obj = MagicMock(owner=request.user)

        self.assertTrue(self.permission.has_object_permission(request, view, obj))

    def test_put_not_owner(self):
        request = MagicMock(user=MagicMock(is_superuser=False))
        view = MagicMock(action='put')
        obj = MagicMock(owner=MagicMock())

        self.assertFalse(self.permission.has_object_permission(request, view, obj))

    def test_put_owner_admin(self):
        request = MagicMock(user=MagicMock(is_superuser=True))
        view = MagicMock(action='put')
        obj = MagicMock(owner=request.user)

        self.assertTrue(self.permission.has_object_permission(request, view, obj))

    def test_put_not_owner_admin(self):
        request = MagicMock(user=MagicMock(is_superuser=True))
        view = MagicMock(action='put')
        obj = MagicMock(owner=MagicMock())

        self.assertFalse(self.permission.has_object_permission(request, view, obj))
