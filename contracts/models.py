from django.db import models

from core.models import BaseModel


class Contract(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    info = models.TextField()

    class Meta:
        ordering = ['id']
