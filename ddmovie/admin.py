from django.contrib import admin

# Register your models here.

from ddmovie.models import Movie, MoviePeople


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
    list_per_page = 20
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
    list_per_page = 20
    list_filter = ('speciality',)
    search_fields = ('name', 'uri')


admin.site.register(MoviePeople, MoviePeopleAdmin)
