from django.contrib import admin

from ddsrc.models import (
    Road,
    Architecture,
    ArchitecturePicture,
    Event,
    EventRelation,
)


class RoadAdmin(admin.ModelAdmin):
    readonly_fields = (
        'name_chs',
        'name_en',
        'des',
        'lib_uri',
        'temporal_value',
        'name_after',
        'history_of_name',
        'history_of_lib_uri',
        'place_name',
        'place_uri',
        'is_from_lib',
        'lib_update_time',
        'update_time',
        'create_time',
    )
    list_display = ('name_chs', 'history_of_name', 'place_name', 'place_name2',
                    'related_place', 'update_time', 'create_time', '_id')
    list_filter = ('place_name',)
    list_per_page = 20
    search_fields = ('name_chs', 'name_en')


admin.site.register(Road, RoadAdmin)


class ArchitecturePictureInline(admin.TabularInline):
    fields = (
        'pic_file',
        'pic_format',
        'des2',
    )
    model = ArchitecturePicture
    extra = 0


class ArchitectureAdmin(admin.ModelAdmin):
    readonly_fields = (
        'name_chs',
        'name_cht',
        'name_en',
        'des',
        'road',
        'road_name_chs',
        'road_lib_uri',
        'address',
        'house_number',
        'longitude',
        'latitude',
        'longitude_bmap',
        'latitude_bmap',
        'is_from_lib',
        'protect_type',
        'lib_uri',
        'place_name',
        'place_uri',
        'batch_no',
        'first_image_uri',
        'first_image_lib_uri',
        'lib_is_red',
        'lib_update_time',
        'update_time',
        'create_time',
    )
    list_display = (
        'name_chs',
        'road_name_chs',
        'place_name',
        'lib_update_time',
	    'hidden',
        'update_time',
        'create_time',
    )
    list_filter = (
        'place_name',
        'lib_is_red',
        'hidden',
    )
    list_per_page = 20
    inlines = [
        ArchitecturePictureInline,
    ]
    search_fields = ('name_chs', 'name_cht', 'name_en', 'road_name_chs')


admin.site.register(Architecture, ArchitectureAdmin)


class EventAdmin(admin.ModelAdmin):
    readonly_fields = (
        'event_title',
        'event_image',
        'event_begin',
        'event_end',
        'uri',
        'raw',
        'update_time',
        'create_time',
    )
    list_display = ('event_title', 'event_image', 'event_begin', 'event_end', 'uri', '_id')
    list_filter = ('event_begin', 'event_end')
    list_per_page = 30
    search_fields = ('event_title', 'uri')

admin.site.register(Event, EventAdmin)


class EventRelationAdmin(admin.ModelAdmin):
    readonly_fields = (
        'event_uri',
        'relation_uri',
        'relation_label',
        'relation_type',
    )
    list_display = ( '_id', 'event_uri', 'relation_uri', 'relation_label', 'relation_type',)
    list_filter = ('relation_type', )
    list_per_page = 30
    search_fields = ('event_uri', 'relation_uri', 'relation_label', )

admin.site.register(EventRelation, EventRelationAdmin)