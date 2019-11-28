from django.urls import path

from . import views

app_name = 'modal'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.BookListView.as_view(), name='index'),
    path('create/', views.BookCreateView.as_view(), name='create_book'),
    path('update/<int:pk>', views.BookUpdateView.as_view(), name='update_book'),
    path('read/<int:pk>', views.BookReadView.as_view(), name='read_book'),
    path('delete/<int:pk>', views.BookDeleteView.as_view(), name='delete_book'),
]
