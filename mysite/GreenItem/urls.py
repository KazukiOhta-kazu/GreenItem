from django.urls import path

from . import views


app_name = 'greenitem'
urlpatterns = [
    path('', views.index, name='index'),
]
