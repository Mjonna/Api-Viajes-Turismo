from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def bienvenida(request):
    return HttpResponse("<h1>API de Viajes y Turismo</h1><p>Bienvenido a la plataforma de gestión de tours y reservas.</p>")
