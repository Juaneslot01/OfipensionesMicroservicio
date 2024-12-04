from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^estudiantes/', views.EstudiantesList),
    url(r'^estudiantescreate/$', csrf_exempt(views.EstudiantesCreate), name='estudiantesCreate'),
    url(r'^createestudiantes/$', csrf_exempt(views.EstudiantesCreate), name='createEstudiantes'),
]