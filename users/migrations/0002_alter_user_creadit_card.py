# Generated by Django 4.2.2 on 2023-07-11 17:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='creadit_card',
            field=models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(16)], verbose_name='Банковская карта'),
        ),
    ]
