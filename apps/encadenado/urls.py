from django.urls import path

from . import views

app_name = 'encadenado'
urlpatterns = [
    path('', views.index, name='index'),
]


