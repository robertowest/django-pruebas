django-pruebas
==============

Pruebas realizadas en django para practicar o para depurar aplicaciones antes de agregarlas a un proyecto productivo.


## Requerimientos

* Python 3.7
* Django 2.2


## Configuraciones

```sh
# django
export DJ_SECRET_KEY=secretkey
export DJ_DEBUG=True

# social-auth
export SOCIAL_AUTH_GITHUB_KEY=xxxxxxxxxxxxxxxxxxxx
export SOCIAL_AUTH_GITHUB_SECRET=yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
```


## Ejecutar

```console
$ pip -c requirements/constraints.txt install -r requirements/develop.txt
$ python manage.py migrate
$ python manage.py insert_dummy_data
$ python manage.py runserver
```


## Contenido

* ajax
* auth2
* books
* [comunes]
* crispy
* domicilio
* encadenado
* modal
* modal2
* progressbar
* prueba
* ubigeo
* uploadFiles

