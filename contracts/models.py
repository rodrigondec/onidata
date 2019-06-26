from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from core.models import BaseModel


class Contract(BaseModel):
    user = models.ForeignKey('users.User',
                             related_name='contracts',
                             on_delete=models.CASCADE,
                             help_text='Usuário do contrato')
    info = models.TextField(help_text='Informações sobre o contrato')
    initial_value = models.FloatField(
        help_text='Valor do contrato',
        validators=[MinValueValidator(limit_value=1)])
    interest_rate = models.FloatField(
        help_text='Porcentagem de juros',
        validators=[MinValueValidator(limit_value=0), MaxValueValidator(limit_value=1)]
    )
    start_date = models.DateField()

    class Meta:
        ordering = ['user_id']

    # noinspection PyTypeChecker,PyUnresolvedReferences
    @property
    def amount_due(self):
        total_paid = 0.0
        for payment in self.payments.all():
            total_paid += payment.value
        return self.value - total_paid
