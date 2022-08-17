from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name='AppCoderInicio'),
    path('cursos/', views.cursos, name='AppCoderCursos'),
    path('profesores/', views.profesores, name='AppCoderProfesores'),
    path('estudiantes/', views.estudiantes, name='AppCoderEstudiantes'),
    path('entregables/', views.entregables, name='AppCoderEntregables')
]