from django.urls import path

from . import views

app_name = 'prueba'
urlpatterns = [
    path('', views.index, name='index'),
    path('tabla/', views.tabla_dinamica.as_view(), name='tabla_dinamica'),
    path('autotabla/', views.autotabla, name='autotabla'),
    path('datos/', views.tabla_datos, name='tabla_datos'),
]


