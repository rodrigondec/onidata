from factory.faker import Faker
from factory import SubFactory

from core.factories import BaseModelFactory
from contracts.models import Contract
from users.factories import UserFactory


class ContractFactory(BaseModelFactory):
    class Meta:
        model = Contract

    user = SubFactory(UserFactory)

    info = Faker('text', max_nb_chars=50)