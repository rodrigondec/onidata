# Generated by Django 2.2.2 on 2019-06-26 20:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_auto_20190626_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='value',
            field=models.DecimalField(decimal_places=2, default=1, help_text='Valor do pagamento', max_digits=1000, validators=[django.core.validators.MinValueValidator(limit_value=1)]),
            preserve_default=False,
        ),
    ]