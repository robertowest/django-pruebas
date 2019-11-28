from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView

from .forms import BookForm
from .models import Book


# def index(request):
#     return render(request, 'modal/index.html')


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book/list.html'


class BookCreateView(BSModalCreateView):
    template_name = 'book/create.html'
    form_class = BookForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('index')


class BookUpdateView(BSModalUpdateView):
    model = Book
    template_name = 'book/update.html'
    form_class = BookForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('index')


class BookReadView(BSModalReadView):
    model = Book
    template_name = 'book/read.html'


class BookDeleteView(BSModalDeleteView):
    model = Book
    template_name = 'book/delete.html'
    success_message = 'Success: Book was deleted.'
    success_url = reverse_lazy('index')
