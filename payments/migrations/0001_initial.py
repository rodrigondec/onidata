# Generated by Django 2.2.3 on 2019-07-07 04:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contracts', '0002_contract_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('value', models.FloatField(help_text='Valor do pagamento', validators=[django.core.validators.MinValueValidator(limit_value=1)])),
                ('date', models.DateField(help_text='Data de pagamento')),
                ('contract', models.ForeignKey(help_text='Contrato do pagamento', on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='contracts.Contract')),
            ],
            options={
                'ordering': ['contract_id'],
            },
        ),
    ]
