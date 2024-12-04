from django.shortcuts import render
from django.http import JsonResponse
from .models import Estudiante
from django.http import HttpResponse
from django.conf import settings
import requests 
import json


def check_acudiente(data):
    r = requests.get(settings.PATH_ACUDIENTE, headers={"Accept": "application/json"})
    acudientes = r.json()
    for acudiente in acudientes:
        if data["acudiente"] == acudiente["id"]:
            return True
    return False



def EstudiantesList(request):
    queryset = Estudiante.objects.all()
    context = list(queryset.values('nombre','apellido','email','telefono','acudiente'))
    return JsonResponse(context,safe=False)

def EstudiantesCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_acudiente(data_json):
            estudiante = Estudiante()
            estudiante.nombre = data_json['nombre']
            estudiante.apellido = data_json['apellido']
            estudiante.email = data_json['email']
            estudiante.telefono = data_json['telefono']
            estudiante.acudiente = data_json['acudiente']
            estudiante.save()
            return JsonResponse({'status':'Creado'})
        else:
            return JsonResponse({'status':'Error'})

def EstudiantesCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        estudiante_list = []
        for estudiante in data_json:
            if check_acudiente(estudiante) == True:
                db_estudiante = Estudiante()
                db_estudiante.nombre = estudiante['nombre']
                db_estudiante.apellido = estudiante['apellido']
                db_estudiante.email = estudiante['email']
                db_estudiante.telefono = estudiante['telefono']
                db_estudiante.acudiente = estudiante['acudiente']
                db_estudiante.save()
                estudiante_list.append(db_estudiante)
            else:
                return HttpResponse('Error')
        Estudiante.objects.bulk_create(estudiante_list)
        return HttpResponse('Creado')
            
