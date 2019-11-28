from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalReadView,
                                           BSModalUpdateView,
                                           BSModalDeleteView)
from django.urls import reverse_lazy
from django.views.generic import ListView

from books.forms import BookForm
from books.models import Book


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/index.html'


class BookCreateView(BSModalCreateView):
    template_name = 'books/create.html'
    form_class = BookForm
    success_message = 'El libro fue creado correctamente.'
    success_url = reverse_lazy('index')


class BookUpdateView(BSModalUpdateView):
    model = Book
    template_name = 'books/update.html'
    form_class = BookForm
    success_message = 'El libro fue actualizado correctamente.'
    success_url = reverse_lazy('index')


class BookReadView(BSModalReadView):
    model = Book
    template_name = 'books/read.html'


class BookDeleteView(BSModalDeleteView):
    model = Book
    template_name = 'books/delete.html'
    success_message = 'El libro fue eliminado correctamente.'
    success_url = reverse_lazy('index')

