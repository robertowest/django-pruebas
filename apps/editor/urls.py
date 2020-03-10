
from django.urls import include, path

from . import views

# https://overiq.com/django-1-10/integrating-ckeditor-in-django/

urlpatterns = [
    path('', views.index, name='ckeditor'),
    path('add/post/', views.add_post, name='add_post'),
    path('edit/post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('ckeditor_uploader/', include('ckeditor_uploader.urls'))
]



# Nos aseguramos de servir los archivos multimedia en desarrollo
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)