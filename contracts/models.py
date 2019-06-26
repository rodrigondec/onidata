from django.db import models
from django.core.validators import MinValueValidator

from core.models import BaseModel


class Contract(BaseModel):
    user = models.ForeignKey('users.User',
                             related_name='contracts',
                             on_delete=models.CASCADE,
                             help_text='Usuário do contrato')
    info = models.TextField(help_text='Informações sobre o contrato')
    value = models.FloatField(
        help_text='Valor do pagamento',
        validators=[MinValueValidator(limit_value=1)])

    class Meta:
        ordering = ['user_id']
