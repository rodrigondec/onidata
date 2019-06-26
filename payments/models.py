from django.db import models
from django.core.validators import MinValueValidator

from core.models import BaseModel


class Payment(BaseModel):
    contract = models.ForeignKey('contracts.Contract',
                                 related_name='payments',
                                 on_delete=models.CASCADE,
                                 help_text='Contrato do pagamento')
    value = models.FloatField(
        help_text='Valor do pagamento',
        validators=[MinValueValidator(limit_value=1)])

    class Meta:
        ordering = ['contract_id']
