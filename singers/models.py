from typing import Any

from django.db import models

from .validators import validate_year


class Singer(models.Model):
    """Исполнитель."""

    name = models.CharField(
        verbose_name='Исполнитель',
        max_length=70,
    )

    class Meta:
        """Метакласс для модели исполнителя."""

        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self) -> Any:
        """Метод возвращает строковое представление исполнителя."""
        return self.name


class Album(models.Model):
    """Альбом."""

    title = models.CharField(
        verbose_name='Название альбома',
        max_length=250,
        db_index=True,
    )
    singer = models.ForeignKey(
        Singer,
        verbose_name='Исполнитель',
        on_delete=models.CASCADE,
        related_name='albums',
    )
    year = models.PositiveIntegerField(
        verbose_name='Год выпуска',
        validators=[validate_year],
        blank=True,
    )

    class Meta:
        """Метакласс для модели альбома."""

        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        ordering = ['-id']

    def __str__(self) -> Any:
        """Метод возвращает строковое представление альбомов."""
        return self.title


class Song(models.Model):
    """Песня."""

    title = models.CharField(
        verbose_name='Название песни',
        max_length=250,
        db_index=True,
    )
    albums = models.ManyToManyField(
        Album,
        through='SongInAlbum',
        related_name='songs',
    )

    class Meta:
        """Метакласс для модели песни."""

        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'
        ordering = ['-id']

    def __str__(self) -> Any:
        """Метод возвращает строковое представление песен."""
        return self.title


class SongInAlbum(models.Model):
    """Песня в альбоме."""

    song = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        verbose_name='Песня в альбоме',
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        verbose_name='Альбом с песней',
    )

    number = models.PositiveSmallIntegerField(
        verbose_name='Порядковый номер',
    )

    class Meta:
        """Метакласс для модели песни в альбоме."""

        verbose_name = 'Песня в альбомах'
        verbose_name_plural = 'Песни в альбомах'
        constraints = [
            models.UniqueConstraint(
                fields=['song', 'number'],
                name='unique_number',
            )
        ]

    def __str__(self) -> Any:
        """Метод возвращает строковое модели."""
        return f'{self.number}: {self.song}'
