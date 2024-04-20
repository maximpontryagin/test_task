from django.contrib import admin
from .models import CustomerProfile, ExecutorProfile


class CustomerProfileAdmin(admin.ModelAdmin):
    """Класс для настройки админки модели заказчика."""

    list_display = (
        'name',
        'contact_info',
        'experience',
    )


class ExecutorProfileAdmin(admin.ModelAdmin):
    """Класс для настройки админки модели исполнителя."""

    list_display = (
        'name',
        'profession',
        'contact_info',
        'experience',
    )


admin.site.register(CustomerProfile, CustomerProfileAdmin)
admin.site.register(ExecutorProfile, ExecutorProfileAdmin)
