from .filters import PersonListFilter
from .forms import PersonFilterFormHelper
from .models import Person
from .tables import PersonsTable
from .utils import PagedFilteredTableView


class PersonListView(PagedFilteredTableView):
    filter_class = PersonListFilter
    model = Person
    table_class = PersonsTable
    template_name = 'table2/person.html'
    formhelper_class = PersonFilterFormHelper

    def get_queryset(self):
        return Person.objects.all()
