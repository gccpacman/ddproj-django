from django.contrib import admin
from rest_framework import serializers

from ddpeotry.models import Peotry

class PeotryAdmin(admin.ModelAdmin):
    readonly_fields = (
        '_id',
        'firstWord',
        'result',
        'status',
        'update_time',
        'create_time',
    )
    list_display = ('_id', 'firstWord', 'result', 'status',)
    list_per_page = 30

admin.site.register(Peotry, PeotryAdmin)