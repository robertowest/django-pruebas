from django import forms
from django.utils.translation import gettext_lazy as _

from crispy_forms.bootstrap import FormActions, InlineField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Fieldset, Layout, Submit


class PersonFilterFormHelper(FormHelper):
    # See https://django-crispy-forms.readthedocs.io/en/latest/form_helper.html

    form_class = "form form-inline"
    form_id = "person-search-form"
    form_method = "GET"
    form_tag = True
    html5_required = True
    layout = Layout(
        Div(
            Fieldset(
                "<span class='fa fa-search'></span> " + str(_("Buscar persona")),
                Div(
                    InlineField("first_name__icontains", wrapper_class="col-4"),
                    InlineField("last_name__icontains", wrapper_class="col-4"),
                    InlineField("id", wrapper_class="col-4"),
                    css_class="row",
                ),
                css_class="col-10 border p-3",
            ),
            FormActions(
                Submit("submit", _("Filtrar")),
                css_class="col-2 text-right align-self-center",
            ),
            css_class="row",
        )
    )
