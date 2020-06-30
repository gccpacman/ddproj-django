from django.contrib import admin

# Register your models here.

from ddmovie.models import Movie, MoviePeople, MoviePhoto


class MovieAdmin(admin.ModelAdmin):
    readonly_fields = (
        'name',
        'raw',
        'detail_raw',
        'movie_type',
        'pub_date',
        'uri',
        'update_time',
        'create_time',
    )
    list_display = ('name', 'uri', 'pub_date')
    list_per_page = 30
    list_filter = ('pub_date',)
    search_fields = ('name', 'uri')


admin.site.register(Movie, MovieAdmin)


class MoviePeopleAdmin(admin.ModelAdmin):
    readonly_fields = (
        'name',
        'raw',
        'speciality',
        'nationality',
        'uri',
        'update_time',
        'create_time',
    )
    list_display = ('name', 'uri', 'speciality', 'nationality')
    list_per_page = 30
    list_filter = ('speciality',)
    search_fields = ('name', 'uri')


admin.site.register(MoviePeople, MoviePeopleAdmin)


class MoviePhotoAdmin(admin.ModelAdmin):
    readonly_fields = (
        'name',
        'raw',
        'image',
        'photoType',
        'uri',
        'update_time',
        'create_time',
    )
    list_display = ('name', 'uri', 'movieUri', 'image', 'photoType')
    list_per_page = 30
    list_filter = ('photoType',)
    search_fields = ('name', 'uri', 'movieUri')

admin.site.register(MoviePhoto, MoviePhotoAdmin)
