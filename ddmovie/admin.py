from django.contrib import admin

# Register your models here.

from ddmovie.models import Movie, MoviePeople, MoviePhoto, MovieCinema, MoviePhotoPeople


class MovieAdmin(admin.ModelAdmin):
    readonly_fields = (
        'name',
        'raw',
        'detail_raw',
        'movie_type',
        'pub_date',
        'formated_pub_date',
        'lib_image_path',
        'uri',
        'update_time',
        'create_time',
    )
    list_display = ('name', 'uri', 'pub_date', 'image', 'first_image_path',)
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
    list_display = ('_id', 'name', 'uri', 'speciality', 'nationality', 'image', 'first_image_path', )
    list_per_page = 30
    list_filter = ('speciality',)
    search_fields = ('name', 'uri')


admin.site.register(MoviePeople, MoviePeopleAdmin)


class MovieCinemaAdmin(admin.ModelAdmin):
    readonly_fields = (
        'name',
        'raw',
        'uri',
        'longitude_bmap',
        'latitude_bmap',
        'update_time',
        'create_time',
        # 'first_image_path'
    )
    list_display = ('_id', 'name', 'uri',)
    list_per_page = 30
    search_fields = ('name', 'uri')


admin.site.register(MovieCinema, MovieCinemaAdmin)


class MoviePhotoAdmin(admin.ModelAdmin):
    readonly_fields = (
        'raw',
        'image',
        'photoType',
        'uri',
        'movieName',
        'movieUri',
        'update_time',
        'create_time',
    )
    list_display = ('_id', 'uri', 'movieUri', 'movieName', 'image', 'photoType', )
    list_per_page = 30
    list_filter = ('photoType',)
    search_fields = ('name', 'uri', 'movieUri')

admin.site.register(MoviePhoto, MoviePhotoAdmin)


class MoviePhotoPeopleAdmin(admin.ModelAdmin):
    readonly_fields = (
        'photoUri',
        'peopleUri',
        'peopleName',
        'update_time',
        'create_time',
    )
    list_display = ('_id', 'photoUri', 'peopleName', 'peopleUri')
    list_per_page = 30
    search_fields = ('peopleName',)

admin.site.register(MoviePhotoPeople, MoviePhotoPeopleAdmin)
