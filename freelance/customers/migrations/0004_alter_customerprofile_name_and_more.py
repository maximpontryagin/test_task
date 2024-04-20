# Generated by Django 4.2 on 2024-04-20 13:59

import customers.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_executorprofile_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='name',
            field=models.CharField(max_length=100, unique=True, validators=[customers.validators.validate_english_and_digits], verbose_name='Имя заказчика'),
        ),
        migrations.AlterField(
            model_name='executorprofile',
            name='name',
            field=models.CharField(max_length=100, unique=True, validators=[customers.validators.validate_english_and_digits], verbose_name='Имя исполнителя'),
        ),
    ]
