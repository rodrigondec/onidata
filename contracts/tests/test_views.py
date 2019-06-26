# Third party
from rest_framework import status

# Project
from core.test_utils import BaseAPITestCase
from contracts.factories import ContractFactory, Contract
from users.factories import UserFactory, User


class ContractsAPITestCase(BaseAPITestCase):
    def setUp(self):
        super().setUp()
        self.endpoint = 'contracts'

    # CREATE
    def test_create_success(self):
        user = UserFactory()
        self.assertEqual(Contract.objects.count(), 0)

        data = {
            'user_id': user.id,
            'info': 'foo'
        }

        path = self.get_path()

        response = self.client.post(path, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.data)
        self.assertEqual(Contract.objects.count(), 1)
        self.assertEqual(Contract.objects.first().user, user)
        self.assertEqual(Contract.objects.first().info, 'foo')

    def test_create_fail(self):
        self.assertEqual(Contract.objects.count(), 0)

        data = {
            'info': 'foo'
        }
        path = self.get_path()

        response = self.client.post(path, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.assertEqual(Contract.objects.count(), 0)

    # PUT
    def test_put_success(self):
        contract = ContractFactory(info='flooo')
        self.assertEqual(Contract.objects.count(), 1)

        self.assertEqual(Contract.objects.first().info, 'flooo')

        data = {
            'user_id': contract.user.id,
            'info': 'foo'
        }
        path = self.get_path(id_detail=contract.id)

        response = self.client.put(path, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(Contract.objects.count(), 1)
        self.assertEqual(Contract.objects.first().user, contract.user)
        self.assertEqual(Contract.objects.first().info, 'foo')

    def test_put_fail(self):
        contract = ContractFactory(info='flooo')
        self.assertEqual(Contract.objects.count(), 1)

        self.assertEqual(Contract.objects.first().info, 'flooo')

        data = {
            'info': 'foo'
        }
        path = self.get_path(id_detail=contract.id)

        response = self.client.put(path, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.assertEqual(Contract.objects.count(), 1)
        self.assertEqual(Contract.objects.first().user, contract.user)
        self.assertEqual(Contract.objects.first().info, 'flooo')

    # PATCH
    def test_patch_success(self):
        contract = ContractFactory(info='flooo')
        self.assertEqual(Contract.objects.count(), 1)

        self.assertEqual(Contract.objects.first().info, 'flooo')

        data = {
            'info': 'foo'
        }
        path = self.get_path(id_detail=contract.id)

        response = self.client.patch(path, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(Contract.objects.count(), 1)
        self.assertEqual(Contract.objects.first().user, contract.user)
        self.assertEqual(Contract.objects.first().info, 'foo')

    def test_patch_fail(self):
        contract = ContractFactory(info='flooo')
        self.assertEqual(Contract.objects.count(), 1)

        self.assertEqual(Contract.objects.first().info, 'flooo')

        data = {
            'info': ''
        }
        path = self.get_path(id_detail=contract.id)

        response = self.client.patch(path, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.assertEqual(Contract.objects.count(), 1)
        self.assertEqual(Contract.objects.first().user, contract.user)
        self.assertEqual(Contract.objects.first().info, 'flooo')

    # LIST
    def test_list_success(self):
        ContractFactory.create_batch(3)
        self.assertEqual(Contract.objects.count(), 3)

        path = self.get_path()

        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(len(response.data.get('results')), 3, msg=response.data)

    # GET
    def test_get_success(self):
        contract = ContractFactory(info='foo')
        self.assertEqual(Contract.objects.count(), 1)

        path = self.get_path(id_detail=contract.id)

        response = self.client.get(path)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(response.data.get('info'), 'foo')

    # DELETE
    def test_delete_success(self):
        contract = ContractFactory()
        self.assertEqual(Contract.objects.count(), 1)

        path = self.get_path(id_detail=contract.id)

        response = self.client.delete(path)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg=response.data)
        self.assertEqual(Contract.objects.count(), 0)
