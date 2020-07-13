from django.contrib import admin

from ddextra.models import TravelPath, TravelPathPoint


class TravelPathPointInline(admin.TabularInline):
    fields = (
        'name',
        'distance',
        'duration',
        'highlight',
        'is_cinema',
    )
    model = TravelPathPoint
    extra = 1


class TravelPathAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'method',
        'duration',
        'feature',
    )
    list_per_page = 20
    inlines = [
        TravelPathPointInline,
    ]
    search_fields = ('name', )


admin.site.register(TravelPath, TravelPathAdmin)
