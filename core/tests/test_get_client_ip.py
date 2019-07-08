from unittest.mock import MagicMock

from django.test import TestCase

from core.utils import get_client_ip


class GetClientIpTestCase(TestCase):
    def test_forwarded(self):
        meta = MagicMock()

        def mocked_get_forwarded(key):
            if key == 'HTTP_X_FORWARDED_FOR':
                return '127.0.0.1,127.0.0.2,127.0.0.3'
            return '127.0.0.4'

        meta.get = mocked_get_forwarded
        request = MagicMock(META=meta)
        self.assertEqual('127.0.0.1', get_client_ip(request))

    def test_remote(self):
        meta = MagicMock()

        def mocked_get_remote(key):
            if key == 'HTTP_X_FORWARDED_FOR':
                return None
            return '127.0.0.4'

        meta.get = mocked_get_remote
        request = MagicMock(META=meta)
        self.assertEqual('127.0.0.4', get_client_ip(request))
