from django.shortcuts import render

def index(request):
    return render(request, 'ajax/index.html', {'message': 'esta es una página AJAX'})


# ---------------------------------------------------------------------------------------


from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    template_name = 'ajax/signup.html'
    form_class = UserCreationForm


# ---------------------------------------------------------------------------------------


from django.contrib.auth.models import User
from django.http import JsonResponse

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'Ya existe un usuario con este nombre de usuario.'
    return JsonResponse(data)


# ---------------------------------------------------------------------------------------


def pass_username(request):
    # username = request.GET.get('username', None)
    # data = {'message': 'El nombre de usuario es %s' % username}
    data = { 'message': 'funciona correctamente' }
    return JsonResponse(data)