from django.test import TestCase

from contracts.factories import ContractFactory, Contract
from payments.factories import PaymentFactory


class ContractTestCase(TestCase):
    def test_create(self):
        ContractFactory()
        self.assertEqual(Contract.objects.count(), 1)

    def test_update(self):
        contract = ContractFactory(info='Informação antiga')
        self.assertEqual(Contract.objects.first().info, 'Informação antiga')

        contract.info = 'Nova informação'
        contract.save()
        self.assertEqual(Contract.objects.first().info, 'Nova informação')

    def test_delete(self):
        contract = ContractFactory()
        self.assertEqual(Contract.objects.count(), 1)

        contract.delete()
        self.assertEqual(Contract.objects.count(), 0)

    def test_amount_due(self):
        contract = ContractFactory(value=150)
        self.assertIsInstance(contract, Contract)

        PaymentFactory.create_batch(2, contract=contract, value=10)

        self.assertEqual(contract.amount_due, 130)
