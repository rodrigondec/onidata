from datetime import date as Date

import pendulum
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
        return self.updated_value - total_paid

    # noinspection PyTypeChecker
    @property
    def updated_value(self):
        today = pendulum.now()
        months_diff = today.diff(self.get_start_date()).in_months()
        return self.initial_value + (self.initial_value * self.interest_rate * months_diff)

    # noinspection PyTypeChecker
    def get_start_date(self):
        isoformat = self.start_date
        if isinstance(self.start_date, Date):
            isoformat = self.start_date.isoformat()
        return pendulum.from_format(isoformat, 'YYYY-MM-DD')
