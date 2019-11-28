from django.shortcuts import render

# Create your views here.
# reordenamiento de los objetos para la página admin
ADMIN_ORDERING = [
    ['domicilio', ['Pais', 'Provincia', 'Localidad']],
    ['prueba', ['Article', 'Post', 'Comment']],
    ['progressbar', ['StuffModel']],
]

def get_app_list(self, request):
    app_dict = self._build_app_dict(request)
    for app_name, object_list in ADMIN_ORDERING:
        app = app_dict[app_name]
        app['models'].sort(key=lambda x: object_list.index(x['object_name']))
        yield app