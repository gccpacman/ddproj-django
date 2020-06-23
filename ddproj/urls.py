from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
# from django.views.static import serve
# from .settings import MEDIA_ROOT

urlpatterns = [
    path('ddad/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/', include("ddsrc.urls")),
    # url(r'^backend/media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]
