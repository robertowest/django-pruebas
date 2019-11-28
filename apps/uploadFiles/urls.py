from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'uploadFiles'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('clear/',                views.clear_database,                  name='clear_database'),
    path('basic-upload/',         views.BasicUploadView.as_view(),       name='basic_upload'),
    path('progress-bar-upload/',  views.ProgressBarUploadView.as_view(), name='progress_bar_upload'),
    path('drag-and-drop-upload/', views.DragAndDropUploadView.as_view(), name='drag_and_drop_upload'),

    path('progress-bar-controller/', views.ProgressBarControllerView.as_view(), name='progress_bar_controller'),
]
