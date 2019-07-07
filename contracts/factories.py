from factory.faker import Faker
from factory import SubFactory

from core.factories import BaseModelFactory
from contracts.models import Contract
from users.factories import UserFactory


class ContractFactory(BaseModelFactory):
    class Meta:
        model = Contract

    client = SubFactory(UserFactory)

    bank = Faker('company')
    amount = Faker('pyfloat', positive=True, right_digits=2, max_value=200, min_value=100)
    interest_rate = Faker('pyfloat', positive=True, right_digits=2, max_value=1, min_value=0)
    submission_date = Faker('date_this_year')
    ip_address = Faker('ipv4_public')
