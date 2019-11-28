from bootstrap_modal_forms.forms import BSModalForm
from .models import Book

class BookForm(BSModalForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price']