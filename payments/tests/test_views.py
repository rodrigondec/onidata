# Third party
from rest_framework import status

# Project
from core.test_utils import BaseAPIJWTTestCase
from payments.factories import PaymentFactory, Payment
from contracts.factories import ContractFactory


class PaymentsAPITestCase(BaseAPIJWTTestCase):
    def setUp(self):
        super().setUp()
        self.endpoint = 'payments'

    # CREATE
    def test_create_success(self):
        contract = ContractFactory()
        self.assertEqual(Payment.objects.count(), 0)
        self.set_user(contract.user)

        data = {
            'contract_id': contract.id,
            'value': 10.5
        }

        path = self.get_path()

        response = self.client.post(path, data=data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, msg=response.data)
        self.assertEqual(Payment.objects.count(), 1)
        self.assertEqual(Payment.objects.first().contract, contract)
        self.assertEqual(Payment.objects.first().value, 10.5)

    def test_create_fail(self):
        contract = ContractFactory()
        self.assertEqual(Payment.objects.count(), 0)
        self.set_user(contract.user)

        data = {
            'contract_id': contract.id,
            'value': -1
        }

        path = self.get_path()

        response = self.client.post(path, data=data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.assertEqual(Payment.objects.count(), 0)

    # PUT
    def test_put_success(self):
        payment = PaymentFactory(value=10.5)
        self.assertEqual(Payment.objects.count(), 1)
        self.set_user(payment.contract.user)

        self.assertEqual(Payment.objects.first().value, 10.5)

        data = {
            'contract_id': payment.contract.id,
            'value': 15
        }
        path = self.get_path(id_detail=payment.id)

        response = self.client.put(path, data=data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(Payment.objects.count(), 1)
        self.assertEqual(Payment.objects.first().contract, payment.contract)
        self.assertEqual(Payment.objects.first().value, 15)

    def test_put_fail(self):
        payment = PaymentFactory(value=10.5)
        self.assertEqual(Payment.objects.count(), 1)
        self.set_user(payment.contract.user)

        self.assertEqual(Payment.objects.first().value, 10.5)

        data = {
            'value': 15
        }
        path = self.get_path(id_detail=payment.id)

        response = self.client.put(path, data=data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.assertEqual(Payment.objects.count(), 1)
        self.assertEqual(Payment.objects.first().contract, payment.contract)
        self.assertEqual(Payment.objects.first().value, 10.5)

    # PATCH
    def test_patch_success(self):
        payment = PaymentFactory(value=10.5)
        self.assertEqual(Payment.objects.count(), 1)
        self.set_user(payment.contract.user)

        self.assertEqual(Payment.objects.first().value, 10.5)

        data = {
            'value': 15
        }
        path = self.get_path(id_detail=payment.id)

        response = self.client.patch(path, data=data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(Payment.objects.count(), 1)
        self.assertEqual(Payment.objects.first().contract, payment.contract)
        self.assertEqual(Payment.objects.first().value, 15)

    def test_patch_fail(self):
        payment = PaymentFactory(value=10.5)
        self.assertEqual(Payment.objects.count(), 1)
        self.set_user(payment.contract.user)

        self.assertEqual(Payment.objects.first().value, 10.5)

        data = {
            'value': 0
        }
        path = self.get_path(id_detail=payment.id)

        response = self.client.patch(path, data=data, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.data)
        self.assertEqual(Payment.objects.count(), 1)
        self.assertEqual(Payment.objects.first().contract, payment.contract)
        self.assertEqual(Payment.objects.first().value, 10.5)

    # LIST
    def test_list_success(self):
        contract = ContractFactory()
        PaymentFactory.create_batch(3, contract=contract)
        self.assertEqual(Payment.objects.count(), 3)
        self.set_user(contract.user)

        path = self.get_path()

        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(len(response.data.get('results')), 3, msg=response.data)

    # GET
    def test_get_success(self):
        payment = PaymentFactory(value=15)
        self.assertEqual(Payment.objects.count(), 1)
        self.set_user(payment.contract.user)

        path = self.get_path(id_detail=payment.id)

        response = self.client.get(path, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.data)
        self.assertEqual(response.data.get('value'), 15)

    # DELETE
    def test_delete_success(self):
        payment = PaymentFactory(value=15)
        self.assertEqual(Payment.objects.count(), 1)
        self.set_user(payment.contract.user)

        path = self.get_path(id_detail=payment.id)

        response = self.client.delete(path, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, msg=response.data)
        self.assertEqual(Payment.objects.count(), 0)
