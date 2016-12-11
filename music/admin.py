from django.contrib import admin
from .models import Album, Song


class SongAdmin(admin.ModelAdmin):
    list_display = ('song_title', 'album', 'is_favorite')


admin.site.register(Album)
admin.site.register(Song, SongAdmin)
