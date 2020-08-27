import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from .models import Person


class PersonsTable(tables.Table):
    name = tables.Column(order_by=("first_name", "last_name"))
    first_name = tables.Column(orderable=False)
    last_name = tables.Column(orderable=False)
    birth_date = tables.Column(orderable=False)
    id = tables.Column(orderable=False)

    class Meta:
        attrs = {"class": "table table-striped table-hover cabecera-azul"}
        model = Person
        fields = ('id', 'name', 'first_name', 'last_name', 'birth_date')
        empty_text = _(
            "No hay ninguna asignatura que satisfaga los criterios de búsqueda."
        )
        template_name = "django_tables2/bootstrap4.html"
        per_page = 20