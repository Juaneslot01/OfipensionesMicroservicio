from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^acudientes/', views.AcudientesList, name='acudientesList'),
    url(r'^acudientecreate/$', csrf_exempt(views.AcudientesCreate), name='acudienteCreate'),
]