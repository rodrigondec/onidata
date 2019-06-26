from django.test import TestCase

from payments.factories import PaymentFactory, Payment


class PaymentTestCase(TestCase):
    def test_create(self):
        PaymentFactory()
        self.assertEqual(Payment.objects.count(), 1)

    def test_update(self):
        payment = PaymentFactory(value=10.50)
        self.assertEqual(Payment.objects.first().value, 10.50)

        payment.value = 15
        payment.save()
        self.assertEqual(Payment.objects.first().value, 15.00)

    def test_delete(self):
        payment = PaymentFactory()
        self.assertEqual(Payment.objects.count(), 1)

        payment.delete()
        self.assertEqual(Payment.objects.count(), 0)
