from django.shortcuts import render
from django.http import JsonResponse
from .models import Acudiente
from django.http import HttpResponse
import json



def AcudientesList(request):
    queryset = Acudiente.objects.all()
    context = list(queryset.values('id','nombre'))
    return JsonResponse(context,safe=False)


def AcudientesCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        acudiente = Acudiente()
        acudiente.nombre = data_json['nombre']
        acudiente.save()
        return HttpResponse('Creado')