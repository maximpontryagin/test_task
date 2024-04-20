# Generated by Django 4.2 on 2024-04-20 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя заказчика')),
                ('contact_info', models.CharField(max_length=200, verbose_name='Контактная информация')),
                ('experience', models.TextField(verbose_name='Опыт заказчика')),
            ],
        ),
        migrations.CreateModel(
            name='ExecutorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя исполнителя')),
                ('contact_info', models.CharField(max_length=200, verbose_name='Контактная информация')),
                ('experience', models.TextField(verbose_name='Опыт исполнителя')),
            ],
        ),
    ]
