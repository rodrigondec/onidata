from factory.faker import Faker
from factory import SubFactory

from core.factories import BaseModelFactory
from payments.models import Payment
from contracts.factories import ContractFactory


class PaymentFactory(BaseModelFactory):
    class Meta:
        model = Payment

    contract = SubFactory(ContractFactory)

    info = Faker('pyfloat', positive=True, right_digits=2, max_value=100, min_value=1)
