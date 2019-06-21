from django.db.models import EmailField

from core.models import BaseModel


class User(BaseModel):
    email = EmailField()
