from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy


class TemplateView(TemplateView):
    template_name = "modal2/index.html"

    def post(self, request, **kwargs):
        # my_data = request.POST
        # do something with your data
        context = {}  #  set your context
        return super(TemplateView, self).render_to_response(context)

