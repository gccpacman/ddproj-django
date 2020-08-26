from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

# from django.views.static import serve
# from .settings import MEDIA_ROOT
from libcache.views import profile

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), 
    path('ddad/', admin.site.urls),
    url(r'^$', profile),
    url(r'^api-auth/', include('rest_framework.urls')),
    # url(r'^api/', include("ddsrc.urls")),
    url(r'^app/src/', include("ddsrc.urls")),
    url(r'^app/movie/', include("ddmovie.urls")),
    url(r'^app/extra/', include("ddextra.urls")),
    url(r'^app/peotry/', include("ddpeotry.urls")),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^backend/media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]
