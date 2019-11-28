from django.urls import path

from . import views

app_name = 'progressbar'
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.call_ajax, name='call_ajax'),
]