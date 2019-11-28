from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, CreateView, DetailView, UpdateView, DeleteView

from apps.books.forms import BookForm
from apps.books.models import Book


class BookListView(ListView):
    model = Book
    template_name = 'nomodal/index.html'


class BookView(FormView):
    template_name = 'nomodal/book_view.html'
    # template_name_suffix = '_view'
    form_class = BookForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        return super().form_valid(form)


class BookCreateView(CreateView):
    model = Book
    fields = ('__all__')


class BookReadView(DetailView):
    model = Book


class BookUpdateView(UpdateView):
    model = Book
    fields = ('__all__')
    # template_name_suffix = '_update_form'


class BookDeleteView(DeleteView):
    model = Book

# class BookCreateView(BSModalCreateView):
#     template_name = 'books/create.html'
#     form_class = BookForm
#     success_message = 'El libro fue creado correctamente.'
#     success_url = reverse_lazy('index')
#
#
# class BookUpdateView(BSModalUpdateView):
#     model = Book
#     template_name = 'books/update.html'
#     form_class = BookForm
#     success_message = 'El libro fue actualizado correctamente.'
#     success_url = reverse_lazy('index')
#
#
# class BookReadView(BSModalReadView):
#     model = Book
#     template_name = 'books/read.html'
#
#
# class BookDeleteView(BSModalDeleteView):
#     model = Book
#     template_name = 'books/delete.html'
#     success_message = 'El libro fue eliminado correctamente.'
#     success_url = reverse_lazy('index')
#
