# Generated by Django 2.2.3 on 2019-07-08 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_contract_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='ip_address',
            field=models.GenericIPAddressField(help_text='Endereço ip da submissão'),
        ),
    ]
