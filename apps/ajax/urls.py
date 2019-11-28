from django.urls import path

from . import views

app_name = 'ajax'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('validate_username/', views.validate_username, name='validate_username'),
    path('pass_username/', views.pass_username, name='pass_username'),
]
