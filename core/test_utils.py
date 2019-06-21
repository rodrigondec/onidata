# from rest_framework_jwt.settings import api_settings
from rest_framework.test import APITestCase

# from users.factories import UserFactory


class BaseAPITestCase(APITestCase):

    def setUp(self):
        # self.user = UserFactory()
        # self.user.set_password('test')
        # self.user.save()

        self.endpoint = None

        # jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        # jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        # payload = jwt_payload_handler(self.user)
        # self.token = jwt_encode_handler(payload)

        # self.auth = 'Bearer {}'.format(self.token)

    def get_path(self, id_detail=None, action=None, filter=None):
        if not self.endpoint:
            raise AttributeError('Endpoint não definido')
        path = f'/{self.endpoint}/'
        if id_detail:
            path += f'{id_detail}/'
        if action:
            path += f'{action}/'
        if filter:
            path += f'?{filter}'
        return path
