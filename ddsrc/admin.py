from django.contrib import admin

# Register your models here.

from .models import Road, Architecture, ArchitecturePicture

class RoadAdmin(admin.ModelAdmin):
    # fields = ('title', 'quiz', 'image', 'type', 'for_friends', 'for_friends_weight_type_a', 'jump_question', 'description', 'audio')
    list_display = ('name_chs', 'name_en', 'lib_uri', 'place_uri', 'place_name', 'lib_update_time', 'update_time', 'create_time', )
    list_filter = ('place_name',)
    list_per_page = 20

admin.site.register(Road, RoadAdmin)


admin.site.register(Architecture)
admin.site.register(ArchitecturePicture)
