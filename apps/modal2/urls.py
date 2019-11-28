from django.urls import path

from . import views

app_name = 'modal2'

urlpatterns = [
    path('', views.TemplateView.as_view(), name='index'),
]
