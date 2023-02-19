import datetime

from django.core.exceptions import ValidationError

MIN_YEAR = 1900


def validate_year(year: int) -> None:
    """Проверка года на корректность."""

    current_year = datetime.datetime.now()
    if year < MIN_YEAR or year > current_year.year:
        raise ValidationError('Указан некорректный год!')
