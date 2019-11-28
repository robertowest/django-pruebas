"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('account/', include('social_django.urls', namespace='social')),
    # path('account/', include('django.contrib.auth.urls', namespace='auth')),

    path('ajax/',         include('apps.ajax.urls')),
    path('auth2/',        include('apps.auth2.urls')),
    # path('auth2/',        include('apps.auth2_google.urls', namespace='auth2')),
    path('domicilio/',    include('apps.domicilio.urls')),
    path('pruebas/',      include('apps.prueba.urls')),
    # path('ubigeo/',     include('apps.ubigeo.urls')),
    path('modal/',        include('apps.modal.urls')),
    path('modal2/',       include('apps.modal2.urls')),
    path('books/',        include('apps.books.urls')),
    path('crispy/',       include('apps.crispy.urls')),
    path('progressbar/',  include('apps.progressbar.urls')),
    path('uploadFiles/',  include('apps.uploadFiles.urls')),
]
