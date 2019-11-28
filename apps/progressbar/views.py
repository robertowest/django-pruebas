from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    # return render(request, 'list.html')
    return render(request, 'progressbar.html')


def call_ajax(request):
    # if request.is_ajax():
    #     message = "Yes, AJAX!"
    # else:
    #     message = "Not Ajax"
    message = ""
    current = int(request.GET.get('current', 0)) + 10
    texto = "<div id='mybar' class='progress-bar progress-bar-striped progress-bar-animated bg-warning' style='width:{0}%' role='progressbar' aria-valuenow='{0}' aria-valuemin='0' aria-valuemax='100'>{0}%</div>".format(current)
    if current >= 100:
        texto = "<div id='mybar' class='progress-bar bg-success' style='width:{0}%' role='progressbar' aria-valuenow='{0}' aria-valuemin='0' aria-valuemax='100'>Terminado</div>".format(100)
        message = "Basta ya!"
    return JsonResponse({'message': message, 'html': texto})






