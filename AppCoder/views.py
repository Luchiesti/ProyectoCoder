from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso, Entregable, Estudiante, Profesor
from django.template import loader
# Create your views here.

def crear_curso(request, nombre, camada):
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    plantilla = loader.get_template('curso.html')
    contexto = {
        'nombre': curso.nombre,
        'camada': curso.camada
    }
    documento = plantilla.render(contexto)

    return HttpResponse(documento)