from typing import Any

from django.db import transaction
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from singers.models import Album, Singer, Song, SongInAlbum


class ListSinderSerializer(serializers.ModelSerializer):
    """Сериализатор для списка исполнителей."""

    class Meta:
        model = Singer
        fields = ('name',)


class DetailSingerSerializer(serializers.ModelSerializer):
    """Сериализатор для исполнителя."""

    albums = serializers.SerializerMethodField()

    def get_albums(self, obj: Singer) -> list[str]:
        """Метод получения всех альбомов исполнителя."""
        return [f'{album}' for album in obj.albums.all()]

    class Meta:
        model = Singer
        fields = (
            'name',
            'albums',
        )


class ListAlbumSerializer(serializers.ModelSerializer):
    """Сериализатор для списка альбомов."""

    singer = serializers.CharField(max_length=70)

    def create(self, validated_data: dict) -> Any:
        """Метод для создания альбома."""
        singer_name = validated_data.pop('singer')
        singer_instance, _ = Singer.objects.get_or_create(name=singer_name)
        obj = Album.objects.create(**validated_data, singer=singer_instance)
        return obj

    class Meta:
        model = Album
        fields = (
            'id',
            'title',
            'singer',
            'year',
        )


class DetailAlbumSerializer(serializers.ModelSerializer):
    """Сериализатор для альбома."""

    singer = serializers.StringRelatedField()
    songs = serializers.StringRelatedField()

    def get_songs(self, obj: Album) -> list[str]:
        song_list = SongInAlbum.objects.filter(album=obj)
        return [f'{song}' for song in song_list]

    class Meta:
        model = Album
        fields = (
            'id',
            'title',
            'singer',
            'year',
            'songs',
        )


class SongInAlbumSerializer(serializers.ModelSerializer):
    """Сериализатор для песен в альбоме."""

    album = serializers.CharField(max_length=50)
    song = serializers.CharField(max_length=50)

    def to_representation(self, instance: SongInAlbum) -> Any:
        """Метод для представления песен в альбоме."""
        self.fields['album'] = serializers.StringRelatedField()
        self.fields['song'] = serializers.StringRelatedField()
        return super(SongInAlbumSerializer, self).to_representation(instance)

    @transaction.atomic
    def create(self, validated_data: dict) -> Any:
        """Метод для создания песен в альбоме."""
        album_title = validated_data.pop('album')
        song_title = validated_data.pop('song')
        album_instance = Album.objects.filter(title=album_title).first()
        if not album_instance:
            raise serializers.ValidationError('Такого альбома не существует!')
        song_instance, _ = Song.objects.get_or_create(title=song_title)
        obj = SongInAlbum.objects.create(
            **validated_data, album=album_instance, song=song_instance
        )
        return obj

    class Meta:
        model = SongInAlbum
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=SongInAlbum.objects.all(),
                fields=['song', 'number'],
                message='Порядковый номер песни в альбомах должен отличаться!',
            )
        ]
