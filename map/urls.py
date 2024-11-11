from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("mymap/", include("mymap.urls")),
    path("admin/", admin.site.urls),
]