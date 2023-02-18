from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import AlbumViewSet, SingerViewSet, SongInALbumViewSet

router = DefaultRouter()

router.register(r'singers', SingerViewSet, basename='singers_api')
router.register(r'albums', AlbumViewSet, basename='albums_api')
router.register(r'songs', SongInALbumViewSet, basename='songs_api')

urlpatterns = [
    path('v1/', include(router.urls)),
]
