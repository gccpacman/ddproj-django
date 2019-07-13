from django.contrib import admin

# Register your models here.

from .models import Road, Architecture, ArchitecturePicture

admin.site.register(Road)
admin.site.register(Architecture)
admin.site.register(ArchitecturePicture)
