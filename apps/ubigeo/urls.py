from django.urls import path

from . import views

app_name = 'ubigeo'
urlpatterns = [
    path('', views.index, name='index'),
    path('obtener_provincias_region/', views.provincias_de_la_region, name='provincias'),
    path('obtener_distritos_provincia/', views.distritos_de_la_provincia, name='distritos'),
]
