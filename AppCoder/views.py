from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import Curso, Entregable, Estudiante, Profesor
from django.template import loader

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    contexto = {
        'cursos': {
            'curso1': 'Nombre1',
            'curso2': 'Nombre2',
            'curso3': 'Nombre3',
            'curso4': 'Nombre4',
        }
    }
    return render(request, 'AppCoder/cursos.html', contexto)


def profesores(request):
    return render(request, 'AppCoder/profesores.html')


def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')


def entregables(request):
    return render(request, 'AppCoder/entregables.html')


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
