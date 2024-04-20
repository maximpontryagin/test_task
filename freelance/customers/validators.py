from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_english_and_digits(value):
    """Валидатор. Имя должно содежрать только английские буквы и цифры."""
    if not value.isalnum():
        raise ValidationError(
            _('Имя должно содержать только английские буквы и цифры.'),
            params={'value': value},
        )
