# Third party
from rest_framework import status

# Project
from core.test_utils import BaseAPIJWTTestCase
from users.factories import UserFactory, User


class UsersAPITestCase(BaseAPIJWTTestCase):
    def setUp(self):
        super().setUp()
        self.endpoint = 'users'

    # CREATE
    def test_create_success(self):
        self.assertEqual(User.objects.count(), 0)

        data = {
            'username': 'test',
            'password': 'password',
            'email': 'test@test.com',
            'first_name': 'foo',
            'last_name': 'bar',
            'cpf': '123.123.123-12'
        }

        path = self.get_path()

        response = self.client.post(path, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, 'test')
        self.assertNotEqual(User.objects.first().password, 'password')
        self.assertEqual(User.objects.first().email, 'test@test.com')
        self.assertEqual(User.objects.first().cpf, '123.123.123-12')
        self.assertEqual(User.objects.first().first_name, 'foo')
        self.assertEqual(User.objects.first().last_name, 'bar')

    def test_duplicate_fail(self):
        UserFactory(username='test', email='test@test.com')
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, 'test')
        self.assertEqual(User.objects.first().email, 'test@test.com')

        data = {
            'username': 'test',
            'password': 'password',
            'email': 'test@test.com',
            'first_name': 'foo',
            'last_name': 'bar'
        }

        path = self.get_path()

        response = self.client.post(path, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, 'test')

    def test_create_fail(self):
        self.assertEqual(User.objects.count(), 0)

        data = {
            'username': 'Test'
        }
        path = self.get_path()

        response = self.client.post(path, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.assertEqual(User.objects.count(), 0)

    # PUT
    def test_put_success(self):
        user = UserFactory(first_name='flooo')
        self.assertEqual(User.objects.count(), 1)
        self.set_user(user)

        self.assertEqual(User.objects.first().first_name, 'flooo')

        data = {
            'username': 'test',
            'email': 'test@test.com',
            'first_name': 'foo',
            'last_name': 'bar'
        }
        path = self.get_path(id_detail=user.id)

        response = self.client.put(path, data=data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().first_name, 'foo')

    def test_put_fail(self):
        user = UserFactory(first_name='flooo')
        self.assertEqual(User.objects.count(), 1)
        self.set_user(user)

        self.assertEqual(User.objects.first().first_name, 'flooo')

        data = {
            'first_name': 'foo'
        }
        path = self.get_path(id_detail=user.id)

        response = self.client.put(path, data=data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().first_name, 'flooo')

    # PATCH
    def test_patch_success(self):
        user = UserFactory(first_name='flooo')
        self.assertEqual(User.objects.count(), 1)
        self.set_user(user)

        self.assertEqual(User.objects.first().first_name, 'flooo')

        data = {
            'first_name': 'foo'
        }
        path = self.get_path(id_detail=user.id)

        response = self.client.patch(path, data=data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().first_name, 'foo')

    def test_patch_fail(self):
        user = UserFactory(first_name='flooo')
        self.assertEqual(User.objects.count(), 1)
        self.set_user(user)

        self.assertEqual(User.objects.first().first_name, 'flooo')

        data = {
            'email': ''
        }
        path = self.get_path(id_detail=user.id)

        response = self.client.patch(path, data=data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().first_name, 'flooo')

    # LIST
    def test_list_success(self):
        users = UserFactory.create_batch(3)
        self.assertEqual(User.objects.count(), 3)
        self.set_user(users[0])

        path = self.get_path()

        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(len(response.data.get('results')), 3, msg=response.data)

    # GET
    def test_get_success(self):
        user = UserFactory(first_name='foo')
        self.assertEqual(User.objects.count(), 1)
        self.set_user(user)

        path = self.get_path(id_detail=user.id)

        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(response.data.get('first_name'), 'foo')

    # DELETE
    def test_delete_success(self):
        user = UserFactory()
        self.assertEqual(User.objects.count(), 1)
        self.set_user(user)

        path = self.get_path(id_detail=user.id)

        response = self.client.delete(path, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg=response.data)
        self.assertEqual(User.objects.count(), 0)
