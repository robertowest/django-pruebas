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

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='inicio'),

    # path('accounts/',     include('apps.accounts.urls')),

    # path('ajax/',         include('apps.ajax.urls')),
    # path('domicilio/',    include('apps.domicilio.urls')),
    # path('ckeditor/',     include('apps.editor.urls')),
    # path('pruebas/',      include('apps.prueba.urls')),
    # # path('ubigeo/',     include('apps.ubigeo.urls')),
    path('modal/',        include('apps.modal.urls')),
    path('modal2/',       include('apps.modal2.urls')),
    # path('books/',        include('apps.books.urls')),
    # path('crispy/',       include('apps.crispy.urls')),
    # path('progressbar/',  include('apps.progressbar.urls')),
    # path('uploadFiles/',  include('apps.uploadFiles.urls')),

    path('table2/', include('apps.table2.urls')),
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
