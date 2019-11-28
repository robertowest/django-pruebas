from django import forms

from .models import Book

class BookForm(forms.Form):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price']