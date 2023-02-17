from django.contrib import admin  # type: ignore

from .models import Album, Singer, Song, SongInAlbum


class SongInAlbumInline(admin.TabularInline):
    model = SongInAlbum


class AlbumAdmin(admin.ModelAdmin):
    inlines = (SongInAlbumInline,)
    list_display = ('id', 'title', 'singer', 'year')
    search_fields = ('title', 'singer')
    list_filter = ('singer',)


class SongAdmin(admin.ModelAdmin):
    inlines = (SongInAlbumInline,)
    exclude = ('album',)
    search_fields = ('song',)


admin.site.register(Song, SongAdmin)
admin.site.register(SongInAlbum)
admin.site.register(Singer)
admin.site.register(Album, AlbumAdmin)
