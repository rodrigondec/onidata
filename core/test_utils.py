from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class BaseAPITestCase(APITestCase):

    def setUp(self):
        self.endpoint = None

    def get_path(self, id_detail=None, action=None, _filter=None):
        if not self.endpoint:
            raise AttributeError('Endpoint não definido')
        path = f'/{self.endpoint}/'
        if id_detail:
            path += f'{id_detail}/'
        if action:
            path += f'{action}/'
        if filter:
            path += f'?{_filter}'
        return path


class BaseAPIJWTTestCase(BaseAPITestCase):

    def setUp(self):
        super().setUp()
        self.user = None
        self.token = None
        self.auth = None

    def set_user(self, user):
        self.user = user
        self._set_token()

    def _set_token(self):
        self.token = RefreshToken.for_user(self.user)
        self.auth = f'Bearer {self.token.access_token}'
