# Vistas del ubigeo
from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext, Context

from .formularios import *
from .models import *
from django.http import HttpResponse
import json


# def index(request):
#     form = UbigeoForm()
#
#     context = {
#       'form' : form,
#     }
#
#     return render_to_response('ubigeo.html', context, context_instance=RequestContext(request))

def index(request):
    form = UbigeoForm()
    context = Context({ 'form' : form, })
    return render(request, 'ubigeo.html', context)

def provincias_de_la_region(request,id_region):
    """Devuelve las provincias de la region para ser utilizados por el js"""
    provincias = Provincia.objects.filter(region = id_region)
    provincias = provincias.order_by('codigo')

    resultado = []
    for provincia in provincias:
        datos = {}
        datos['id'] = provincia.id
        datos['nombre'] = provincia.nombre
        resultado.append(datos)

    return HttpResponse( json.dumps(resultado) )


def distritos_de_la_provincia(request,id_provincia):
    """Devuelve los distritos de la provincia para ser utilizados por el js"""
    distritos = Distrito.objects.filter(provincia = id_provincia)
    distritos = distritos.order_by('codigo')

    resultado = []
    for distrito in distritos:
        datos = {}
        datos['id'] = distrito.id
        datos['nombre'] = distrito.nombre
        resultado.append(datos)

    return HttpResponse( json.dumps(resultado) )
