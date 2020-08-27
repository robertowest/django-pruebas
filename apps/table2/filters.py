import django_filters
from .models import Person


class PersonListFilter(django_filters.FilterSet):
    class Meta:
        model = Person
        fields = {
            "first_name": ["icontains"],
            "last_name": ["icontains"],
            "id": ["exact"],
        }
        order_by = ["first_name", "last_name"]
