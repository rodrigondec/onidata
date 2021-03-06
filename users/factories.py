from factory.faker import Faker

from core.factories import BaseModelFactory
from users.models import User


class UserFactory(BaseModelFactory):
    class Meta:
        model = User

    email = Faker('safe_email')
    username = Faker('user_name')
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    cpf = Faker('text', max_nb_chars=14)

    is_staff = False
    is_superuser = False
