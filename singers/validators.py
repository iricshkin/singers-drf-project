import datetime

from django.core.exceptions import ValidationError  # type: ignore


def validate_year(year: int) -> None:
    """Проверка года на корректность."""

    current_year = datetime.datetime.now()
    if year < 1900 or year > current_year.year:
        raise ValidationError('Указан екорректный год!')
