from django.db import models
from django.core.validators import MinValueValidator

from core.models import BaseModel


class Payment(BaseModel):
    contract = models.ForeignKey('contracts.Contract', on_delete=models.CASCADE, help_text='Contrato do pagamento')
    value = models.DecimalField(
        decimal_places=2,
        max_digits=1000,
        help_text='Valor do pagamento',
        validators=[MinValueValidator(limit_value=1)])

    class Meta:
        ordering = ['contract_id']
