import uuid

from factory import DjangoModelFactory, lazy_attribute

from .models import BaseModel


class BaseModelFactory(DjangoModelFactory):

    class Meta:
        model = BaseModel
        abstract = True

    id = lazy_attribute(lambda x: uuid.uuid4())
