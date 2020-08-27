from django.urls import path

from . import views

app_name = 'table2'

urlpatterns = [
    path('', views.PersonListView.as_view())
]
