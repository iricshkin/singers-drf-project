from django.contrib import admin  # type: ignore
from django.urls import include, path, re_path  # type: ignore
from drf_yasg import openapi  # type: ignore
from drf_yasg.views import get_schema_view  # type: ignore
from rest_framework import permissions  # type: ignore

schema_view = get_schema_view(
    openapi.Info(
        title='Singers API',
        default_version='v1',
        description='Документация для приложения Singers',
        contact=openapi.Contact(email='admin@singers.ru'),
        license=openapi.License(name='MIT License '),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    re_path(
        r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
]
