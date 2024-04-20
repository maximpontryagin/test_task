from django.db import models
from . import validators


class CustomerProfile(models.Model):
    """Модель заказчика."""

    name = models.CharField(max_length=100,
                            verbose_name='Имя заказчика',
                            unique=True,
                            validators=[validators.validate_english_and_digits])
    contact_info = models.CharField(max_length=200,
                                    verbose_name='Контактная информация')
    experience = models.TextField(verbose_name='Опыт заказчика')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики' 


class ExecutorProfile(models.Model):
    """Модель исполнителя."""

    name = models.CharField(max_length=100,
                            verbose_name='Имя исполнителя',
                            unique=True,
                            validators=[validators.validate_english_and_digits])
    contact_info = models.CharField(max_length=200,
                                    verbose_name='Контактная информация')
    profession = models.CharField(max_length=200, verbose_name='Профессия')
    experience = models.TextField(verbose_name='Опыт исполнителя')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'
