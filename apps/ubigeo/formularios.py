#-*- coding: utf-8 -*-
"""Archivos formularios.py donde están los formularios del ubigeo"""

from django import forms

from .models import *
from django.utils.translation import ugettext as _

from datetime import time
import datetime


class UbigeoForm(forms.Form):
    """Formulario del ubigeo"""

    def __init__(self, *args, **kwargs):

        super(UbigeoForm, self).__init__(*args, **kwargs)

        self.fields['region'] =  forms.TypedChoiceField(
               label = _(u'Elija region'),
               choices = self.regiones(),
               coerce = int,
               required=True,
               widget=forms.Select(attrs={'id':'combo_region',
                                   'onchange':'actualizar_provincia()'}))

        self.fields['provincia'] =  forms.TypedChoiceField(
               label = _(u'Elija provincia'),
               choices = self.provincia(),
               coerce = int,
               required=True,
               widget=forms.Select(attrs={'id':'combo_provincia',
                                   'onchange':'actualizar_distrito()'}))

        self.fields['distrito'] =  forms.TypedChoiceField(
               label = _(u'Elija distrito'),
               choices = self.distrito(),
               coerce = int,
               required=True,
               widget=forms.Select(attrs={'id':'combo_distrito'}))

    def regiones(self):
      # Devuelve el origen posible de las reservaciones
      regiones = Region.objects.all().order_by('codigo')
      resultado = []
      for region in regiones:
          tupla = (region.id, region.nombre)
          resultado.append(tupla)
      return resultado

    def provincia(self):
      # Devuelve el origen posible de las reservaciones
      provincias = Provincia.objects.filter(region__codigo = 1)
      provincias = provincias.order_by('codigo')
      resultado = []
      for provincia in provincias:
          tupla = (provincia.id, provincia.nombre)
          resultado.append(tupla)
      return resultado

    def distrito(self):
      # Devuelve el origen posible de las reservaciones
      distritos = Distrito.objects.filter(provincia__codigo = 1)
      distritos = distritos.order_by('codigo')
      resultado = []
      for distrito in distritos:
          tupla = (distrito.id, distrito.nombre)
          resultado.append(tupla)
      return resultado
