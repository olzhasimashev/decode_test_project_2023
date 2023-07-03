# Generated by Django 3.2.5 on 2023-07-03 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField(max_length=200)),
                ('color', models.CharField(blank=True, default='white', max_length=35)),
            ],
        ),
    ]