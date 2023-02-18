from typing import Any

from rest_framework import viewsets

from api.serializers import (DetailAlbumSerializer, DetailSingerSerializer,
                             ListAlbumSerializer, ListSinderSerializer,
                             SongInAlbumSerializer)
from singers.models import Album, Singer, SongInAlbum


class SingerViewSet(viewsets.ModelViewSet):
    """Класс представления для исполнителей."""

    serializer_class = ListSinderSerializer
    queryset = Singer.objects.all()
    detail_serializer_class = DetailSingerSerializer

    def get_serializer_class(self) -> Any:
        """Метод определения класса сериализатора."""

        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super(SingerViewSet, self).get_serializer_class()


class AlbumViewSet(viewsets.ModelViewSet):
    """Класс представления для альбомов."""

    queryset = Album.objects.all()
    serializer_class = ListAlbumSerializer
    detail_serializer_class = DetailAlbumSerializer

    def get_serializer_class(self) -> Any:
        """Метод определения класса сериализатора."""
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super(AlbumViewSet, self).get_serializer_class()

    def perform_update(self, serializer: DetailAlbumSerializer) -> None:
        """Метод обновления альбома."""
        singer_instance, _ = Singer.objects.get_or_create(
            name=self.request.data['singer']
        )
        serializer.save(singer=singer_instance)


class SongInALbumViewSet(viewsets.ModelViewSet):
    """Класс представления для песен в альбомах."""

    queryset = SongInAlbum.objects.all()
    serializer_class = SongInAlbumSerializer
