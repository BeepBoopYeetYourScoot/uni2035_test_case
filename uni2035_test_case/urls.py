from django.contrib import admin
from django.urls import path, include
from regions.routers import urlpatterns as region_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(region_urls))
]
