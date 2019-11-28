from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import include, path

from . import views

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path('', views.manage, name='manage'),
    path('logout/', LogoutView.as_view(template_name=settings.LOGOUT_REDIRECT_URL), name='logout'),
]

