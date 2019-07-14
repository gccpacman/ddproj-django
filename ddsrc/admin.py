from django.contrib import admin

# Register your models here.

from .models import Road, Architecture, ArchitecturePicture

class RoadAdmin(admin.ModelAdmin):
    readonly_fields = ('name_chs', 'name_en', 'des', 'lib_uri', 'temporal_value', 'history_of_name', 'name_after', 'history_of_lib_uri', 'place_name', 'place_uri', 'is_from_lib', 'lib_update_time', 'update_time', 'create_time',)
    list_display = ('name_chs', 'lib_uri', 'place_name', 'lib_update_time', 'update_time', 'create_time', )
    list_filter = ('place_name',)
    list_per_page = 20

admin.site.register(Road, RoadAdmin)


class ArchitecturePictureInline(admin.TabularInline):
    fields = ('pic_file', 'pic_format', 'des2', )
    model = ArchitecturePicture
    extra = 0

class ArchitectureAdmin(admin.ModelAdmin):
    readonly_fields = ('name_chs', 'name_cht', 'name_en', 'des', 'road', 'road_name_chs', 'road_lib_uri', 'address', 'house_number', 'longitude', 'latitude', 'is_from_lib', 'protect_type', 'lib_uri', 'place_name', 'place_uri', 'batch_no', 'first_image_uri', 'first_image_path', 'lib_update_time', 'update_time', 'create_time',)
    list_display = ('name_chs', 'lib_uri', 'place_name', 'lib_update_time', 'update_time', 'create_time', )
    list_filter = ('place_name',)
    list_per_page = 20
    inlines = [
        ArchitecturePictureInline,
    ]

admin.site.register(Architecture, ArchitectureAdmin)
# admin.site.register(ArchitecturePicture)
