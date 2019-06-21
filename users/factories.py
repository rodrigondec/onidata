from factory.faker import Faker

from core.factories import BaseModelFactory
from users.models import User


class UserFactory(BaseModelFactory):
    class Meta:
        model = User

    username = Faker('user_name')
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    email = Faker('safe_email')

