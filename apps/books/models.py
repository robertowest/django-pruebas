from django.db import models
from django.urls import reverse


class Book(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    BOOK_TYPES = (
        (HARDCOVER, 'Hardcover'),
        (PAPERBACK, 'Paperback'),
        (EBOOK, 'E-book'),
    )
    title = models.CharField(max_length=50)
    publication_date = models.DateField(null=True)
    author = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES)
    timestamp = models.DateField(auto_now_add=True, auto_now=False)

    def get_absolute_url(self):
        return reverse('read', kwargs={'pk': self.pk})

    def get_fields(self):
        """Devuelve una lista con todos los nombres de campo de la entidad."""
        fields = []

        # descarta los campos especiales y los campos sin valor
        descarte = ('id', 'active', 'created', 'created_by', 'modified', 'modified_by')

        for f in self._meta.fields:
            fname = f.name
            try:
                value = getattr(self, fname)
                if len(f.flatchoices) > 0:
                    value = dict(f.flatchoices).get(value)

            except:
                value = None
            if f.editable and value and f.name not in descarte:
                fields.append({'name': f.verbose_name, 'value': value, 'type': f.get_internal_type()})
        return fields