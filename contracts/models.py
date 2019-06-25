from django.db import models

from core.models import BaseModel


class Contract(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, help_text='Usuário do contrato')
    info = models.TextField(help_text='Informações sobre o contrato')

    class Meta:
        ordering = ['id']
