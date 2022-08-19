from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from AppCoder.forms import CursoForm, BuscadorCurso
from AppCoder.models import Curso


def inicio(request):
    return render(request, 'AppCoder/inicio.html')


def buscar_curso(request):
    curso_buscar = []
    if request.method == 'POST':
        camada = request.POST.get('camada')
        curso_buscar = Curso.objects.filter(camada__exact=camada)


    contexto = {
        'my_form': BuscadorCurso(),
        'cursos': curso_buscar,
    }
    return render(request, 'AppCoder/buscar_curso.html', contexto)


def cursos(request):

    if request.method == 'POST':
        my_form = CursoForm(request.POST)

        if my_form.is_valid():
            data = my_form.cleaned_data

            curso_data = Curso(nombre=data.get('nombre'), camada=data.get('camada'))
            curso_data.save()

    cursos = Curso.objects.all()
    contexto = {
        'cursos':cursos,
        'my_form': CursoForm(),

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
