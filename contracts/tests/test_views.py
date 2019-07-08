# Third party
from rest_framework import status

# Project
from core.test_utils import BaseAPIJWTTestCase
from contracts.factories import ContractFactory, Contract
from users.factories import UserFactory


class ContractsAPITestCase(BaseAPIJWTTestCase):
    def setUp(self):
        super().setUp()
        self.endpoint = 'contracts'

    # CREATE
    def test_create_success(self):
        user = UserFactory()
        self.assertEqual(Contract.objects.count(), 0)
        self.set_user(user)

        data = {
            'client_id': user.id,
            'bank': 'foo',
            'amount': 150,
            'interest_rate': 1,
            'submission_date': '2019-01-01'
        }

        path = self.get_path()

        response = self.client.post(path, data=data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.data)
        self.assertEqual(Contract.objects.count(), 1)
        self.assertEqual(Contract.objects.first().client, user)
        self.assertEqual(Contract.objects.first().bank, 'foo')
        self.assertEqual(Contract.objects.first().amount, 150)
        self.assertEqual(Contract.objects.first().interest_rate, 1)
        self.assertEqual(Contract.objects.first().submission_date.isoformat(), '2019-01-01')
        self.assertEqual(Contract.objects.first().ip_address, '127.0.0.1')

    def test_create_fail(self):
        user = UserFactory()
        self.assertEqual(Contract.objects.count(), 0)
        self.set_user(user)

        data = {
            'bank': 'foo'
        }
        path = self.get_path()

        response = self.client.post(path, data=data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.assertEqual(Contract.objects.count(), 0)

    # PUT
    def test_put_success(self):
        contract = ContractFactory(bank='flooo')
        self.assertEqual(Contract.objects.count(), 1)
        self.set_user(contract.client)

        self.assertEqual(Contract.objects.first().bank, 'flooo')

        data = {
            'client_id': contract.client.id,
            'bank': 'foo',
            'amount': 150,
            'interest_rate': 0,
            'submission_date': '2019-01-01'
        }
        path = self.get_path(id_detail=contract.id)

        response = self.client.put(path, data=data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(Contract.objects.count(), 1)
        self.assertEqual(Contract.objects.first().client, contract.client)
        self.assertEqual(Contract.objects.first().bank, 'foo')
        self.assertEqual(Contract.objects.first().amount, 150)
        self.assertEqual(Contract.objects.first().interest_rate, 0)
        self.assertEqual(Contract.objects.first().submission_date.isoformat(), '2019-01-01')

    def test_put_fail_missing_field(self):
        contract = ContractFactory(bank='flooo')
        self.assertEqual(Contract.objects.count(), 1)
        self.set_user(contract.client)

        self.assertEqual(Contract.objects.first().bank, 'flooo')

        data = {
            'bank': 'foo'
        }
        path = self.get_path(id_detail=contract.id)

        response = self.client.put(path, data=data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.assertEqual(Contract.objects.count(), 1)
        self.assertEqual(Contract.objects.first().client, contract.client)
        self.assertEqual(Contract.objects.first().bank, 'flooo')

    def test_put_fail_unauthorized(self):
        contract = ContractFactory(bank='flooo')
        self.assertEqual(Contract.objects.count(), 1)
        self.set_user(UserFactory())

        self.assertEqual(Contract.objects.first().bank, 'flooo')

        data = {
            'client_id': contract.client.id,
            'bank': 'foo',
            'amount': 150,
            'interest_rate': 0,
            'submission_date': '2019-01-01'
        }
        path = self.get_path(id_detail=contract.id)

        response = self.client.put(path, data=data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=response.data)
        self.assertEqual(Contract.objects.first().bank, 'flooo')

    # PATCH
    def test_patch_success(self):
        contract = ContractFactory(bank='flooo')
        self.assertEqual(Contract.objects.count(), 1)
        self.set_user(contract.client)

        self.assertEqual(Contract.objects.first().bank, 'flooo')

        data = {
            'bank': 'foo'
        }
        path = self.get_path(id_detail=contract.id)

        response = self.client.patch(path, data=data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(Contract.objects.count(), 1)
        self.assertEqual(Contract.objects.first().client, contract.client)
        self.assertEqual(Contract.objects.first().bank, 'foo')

    def test_patch_fail(self):
        contract = ContractFactory(bank='flooo')
        self.assertEqual(Contract.objects.count(), 1)
        self.set_user(contract.client)

        self.assertEqual(Contract.objects.first().bank, 'flooo')

        data = {
            'bank': ''
        }
        path = self.get_path(id_detail=contract.id)

        response = self.client.patch(path, data=data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.assertEqual(Contract.objects.count(), 1)
        self.assertEqual(Contract.objects.first().client, contract.client)
        self.assertEqual(Contract.objects.first().bank, 'flooo')

    # LIST
    def test_list_success(self):
        user = UserFactory()
        ContractFactory.create_batch(3, client=user)
        self.assertEqual(Contract.objects.count(), 3)
        self.set_user(user)

        path = self.get_path()

        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(len(response.data.get('results')), 3, msg=response.data)

    def test_list_two_users_success(self):
        user = UserFactory()
        ContractFactory.create_batch(3, client=user)
        self.assertEqual(Contract.objects.count(), 3)
        self.set_user(user)

        path = self.get_path()

        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(len(response.data.get('results')), 3, msg=response.data)

        user2 = UserFactory()
        ContractFactory.create_batch(2, client=user2)
        self.assertEqual(Contract.objects.count(), 5)
        self.set_user(user2)

        path = self.get_path()

        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(len(response.data.get('results')), 2, msg=response.data)

    def test_list_admin_success(self):
        user = UserFactory()
        ContractFactory.create_batch(3, client=user)
        self.assertEqual(Contract.objects.count(), 3)

        admin = UserFactory(is_staff=True, is_superuser=True)
        self.set_user(admin)

        path = self.get_path()

        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(len(response.data.get('results')), 3, msg=response.data)

    # GET
    def test_get_success(self):
        contract = ContractFactory(bank='foo')
        self.assertEqual(Contract.objects.count(), 1)
        self.set_user(contract.client)

        path = self.get_path(id_detail=contract.id)

        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(response.data.get('bank'), 'foo')

    def test_get_admin_success(self):
        contract = ContractFactory(bank='foo')
        self.assertEqual(Contract.objects.count(), 1)

        self.set_user(UserFactory(is_staff=True, is_superuser=True))

        path = self.get_path(id_detail=contract.id)

        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(response.data.get('bank'), 'foo')

    def test_get_fail_unauthorized(self):
        contract = ContractFactory(bank='foo')
        self.assertEqual(Contract.objects.count(), 1)

        self.set_user(UserFactory())

        path = self.get_path(id_detail=contract.id)

        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=response.data)

    # DELETE
    def test_delete_success(self):
        contract = ContractFactory()
        self.assertEqual(Contract.objects.count(), 1)
        self.set_user(contract.client)

        path = self.get_path(id_detail=contract.id)

        response = self.client.delete(path, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg=response.data)
        self.assertEqual(Contract.objects.count(), 0)

    def test_delete_fail_unauthorized(self):
        contract = ContractFactory()
        self.assertEqual(Contract.objects.count(), 1)

        self.set_user(UserFactory())

        path = self.get_path(id_detail=contract.id)

        response = self.client.delete(path, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, msg=response.data)
        self.assertEqual(Contract.objects.count(), 1)
