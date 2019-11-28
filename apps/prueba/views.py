from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, 'index.html')


class tabla_dinamica(TemplateView):
      template_name = 'tabla_dinamica.html'

      def get_context_data(self, **kwargs):
            ctx = super().get_context_data(**kwargs)
            ctx['header'] = ['#', 'chemblID','Preferable Name']
            ctx['rows'] = [{'id':10, 'chemblid':534988, 'prefName':'A'},
                           {'id':20, 'chemblid':312920, 'prefName':'B'},
                           {'id':30, 'chemblid':987615, 'prefName':'C'}]
            return ctx


def tabla_datos(request):
    template_name = 'tabla_datos.html'



def autotabla(request):
    return render(request, 'autotabla.html')

def events_index(request):
    template_name = 'table2.html'

    # # este funciona agrupando paises y provincias 
    # paises = Pais.objects.all()
    # group = {}
    # for pais in paises:
    #     provincia_key = '_'.join([str(provincia.pk) for provincia in pais.provincia_set.all()])
    #     if not provincia_key in group and provincia_key != '':
    #         group[provincia_key] = {'provincias': pais.provincia_set.all(), 'paises': []}
    #     if provincia_key != '':
    #         group[provincia_key]['paises'].append(pais)


# def events_index(request, year):
#     template_name = 'table3.html'
#
#     selected_year = Year.objects.get(title=year)
#     events_list = Event.objects.filter(year = selected_year.id).order_by('category','start_date')
#     return render_to_response('events_list.html', {"events_list": events_list})
#
#
# {% regroup events_list by category.title as events_list_by_category %}
# {% for category in events_list_by_category %}
#     <hr>
#     <h2>{{ category.grouper }}</h2>
#     {% regroup category.list by start_date.month as events_list_by_month %}
#     {% for month in events_list_by_month %}
#         <h3>{{ month.grouper }}</h3>
#         {% for event in month.list %}
#             <h4>{{ event.title }}</h4>
#             <p>{{ event.start_date }}</p>
#             <p>{{ event.category.title }}</p>
#         {% endfor %}
#     {% endfor %}
# {% endfor %}