# Third party
from rest_framework import status

# Project
from core.test_utils import BaseAPITestCase
from contracts.factories import ContractFactory, Contract
from users.factories import UserFactory, User
from payments.factories import PaymentFactory, Payment


class UsersAPITestCase(BaseAPITestCase):
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
            'last_name': 'bar'
        }

        path = self.get_path()

        response = self.client.post(path, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, 'test')
        self.assertNotEqual(User.objects.first().password, 'password')
        self.assertEqual(User.objects.first().email, 'test@test.com')
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

        self.assertEqual(User.objects.first().first_name, 'flooo')

        data = {
            'username': 'test',
            'email': 'test@test.com',
            'first_name': 'foo',
            'last_name': 'bar'
        }
        path = self.get_path(id_detail=user.id)

        response = self.client.put(path, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().first_name, 'foo')

    def test_put_fail(self):
        user = UserFactory(first_name='flooo')
        self.assertEqual(User.objects.count(), 1)

        self.assertEqual(User.objects.first().first_name, 'flooo')

        data = {
            'first_name': 'foo'
        }
        path = self.get_path(id_detail=user.id)

        response = self.client.put(path, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().first_name, 'flooo')

    # PATCH
    def test_patch_success(self):
        user = UserFactory(first_name='flooo')
        self.assertEqual(User.objects.count(), 1)

        self.assertEqual(User.objects.first().first_name, 'flooo')

        data = {
            'first_name': 'foo'
        }
        path = self.get_path(id_detail=user.id)

        response = self.client.patch(path, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().first_name, 'foo')

    def test_patch_fail(self):
        user = UserFactory(first_name='flooo')
        self.assertEqual(User.objects.count(), 1)

        self.assertEqual(User.objects.first().first_name, 'flooo')

        data = {
            'email': ''
        }
        path = self.get_path(id_detail=user.id)

        response = self.client.patch(path, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().first_name, 'flooo')

    # LIST
    def test_list_success(self):
        UserFactory.create_batch(3)
        self.assertEqual(User.objects.count(), 3)

        path = self.get_path()

        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(len(response.data.get('results')), 3, msg=response.data)

    # GET
    def test_get_success(self):
        user = UserFactory(first_name='foo')
        self.assertEqual(User.objects.count(), 1)

        path = self.get_path(id_detail=user.id)

        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(response.data.get('first_name'), 'foo')

    # DELETE
    def test_delete_success(self):
        user = UserFactory()
        self.assertEqual(User.objects.count(), 1)

        path = self.get_path(id_detail=user.id)

        response = self.client.delete(path)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg=response.data)
        self.assertEqual(User.objects.count(), 0)

    # NESTED VIEW SETS
    def test_contracts_list(self):
        user = UserFactory()
        self.assertEqual(User.objects.count(), 1)

        ContractFactory.create_batch(3, user=user)
        self.assertEqual(Contract.objects.count(), 3)

        path = self.get_path(id_detail=user.id, action='contracts')

        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(len(response.data.get('results')), 3, msg=response.data)

    def test_contracts_get(self):
        user = UserFactory()
        self.assertEqual(User.objects.count(), 1)

        contract = ContractFactory(user=user, info='foo')
        self.assertEqual(Contract.objects.count(), 1)

        path = self.get_path(id_detail=user.id, action=f'contracts/{contract.id}')

        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(response.data.get('info'), 'foo')

    def test_payments_list(self):
        user = UserFactory()
        self.assertEqual(User.objects.count(), 1)

        contract = ContractFactory(user=user, info='foo')
        self.assertEqual(Contract.objects.count(), 1)

        PaymentFactory.create_batch(3, contract=contract, value=15)
        self.assertEqual(Payment.objects.count(), 3)

        path = self.get_path(id_detail=user.id, action='payments')

        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(len(response.data.get('results')), 3, msg=response.data)

    def test_payments_get(self):
        user = UserFactory()
        self.assertEqual(User.objects.count(), 1)

        contract = ContractFactory(user=user, info='foo')
        self.assertEqual(Contract.objects.count(), 1)

        payment = PaymentFactory(contract=contract, value=15)
        self.assertEqual(Payment.objects.count(), 1)

        path = self.get_path(id_detail=user.id, action=f'payments/{payment.id}')

        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(response.data.get('value'), '15.00')
