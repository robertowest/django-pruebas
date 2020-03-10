from django.contrib.auth.views import TemplateView
from django.urls import include, path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', TemplateView.as_view(template_name='accounts/index.html'), name='index'),
    
    path('', include('django.contrib.auth.urls', namespace='auth')),
    path('', include('social_django.urls', namespace='social')),

    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/', views.update_profile),
    path('logout/', views.Logout),
]
