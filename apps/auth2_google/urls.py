from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import include, path

from . import views

# https://medium.com/@jainsahil1997/simple-google-authentication-in-django-58101a34736b

urlpatterns = [
    path('', views.manage, name='home'),
    path('profile/', views.update_profile),
    path('account/logout/', views.Logout),
]
