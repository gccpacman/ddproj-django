from django.contrib import admin

from ddextra.models import TravelPath, TravelPathPoint, RichTextArticle


class TravelPathPointInline(admin.TabularInline):
    fields = (
        'name',
        'architecture_id',
        'distance',
        'address',
        'duration',
        'highlight',
        'image',
        'longitude',
        'latitude',
        'priority',
        'is_cinema',
    )
    model = TravelPathPoint
    extra = 1


class TravelPathAdmin(admin.ModelAdmin):
    list_display = (
        '_id',
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


class RichTextArticleAdmin(admin.ModelAdmin):
    list_display = (
        '_id',
        'title',
    )
    list_per_page = 20
    search_fields = ('title', )

admin.site.register(RichTextArticle, RichTextArticleAdmin)