from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('greenitem/', include('greenitem.urls')),
    path('admin/', admin.site.urls),
]
