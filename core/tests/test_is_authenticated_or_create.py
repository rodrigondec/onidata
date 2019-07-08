from unittest.mock import MagicMock

from django.test import TestCase

from core.permissions import IsAuthenticatedOrCreate


class IsAuthenticatedOrCreateTestCase(TestCase):
    def setUp(self):
        self.permission = IsAuthenticatedOrCreate()
        self.view = MagicMock()

    def test_logged(self):
        request = MagicMock(method='GET', user=MagicMock(is_authenticated=True))

        self.assertTrue(self.permission.has_permission(request, self.view))

    def test_not_logged(self):
        request = MagicMock(method='GET', user=MagicMock(is_authenticated=False))

        self.assertFalse(self.permission.has_permission(request, self.view))

    def test_create(self):
        request = MagicMock(method='POST', user=MagicMock(is_authenticated=False))

        self.assertTrue(self.permission.has_permission(request, self.view))
