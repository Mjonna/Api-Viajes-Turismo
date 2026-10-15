from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from rest_framework import viewsets

from .models import Destino, Guia, Tour, Cliente, Reserva
from .serializers import (
    DestinoSerializer,
    GuiaSerializer,
    TourSerializer,
    ClienteSerializer,
    ReservaSerializer,
)
def bienvenida(request):
    return render(request, 'bienvenida.html')
@login_required
def panel(request):
    contexto = {
        'total_destinos': Destino.objects.count(),
        'total_tours': Tour.objects.count(),
        'total_clientes': Cliente.objects.count(),
        'total_reservas': Reserva.objects.count(),
    }
    return render(request, 'panel.html', contexto)


class CatalogoToursView(LoginRequiredMixin, ListView):
    model = Tour
    template_name = 'catalogo.html'
    context_object_name = 'tours'
    ordering = ['id']

class DestinoViewSet(viewsets.ModelViewSet):
    queryset = Destino.objects.all().order_by("id")
    serializer_class = DestinoSerializer


class GuiaViewSet(viewsets.ModelViewSet):
    queryset = Guia.objects.all().order_by("id")
    serializer_class = GuiaSerializer


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all().order_by("id")
    serializer_class = TourSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by("id")
    serializer_class = ClienteSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all().order_by("id")
    serializer_class = ReservaSerializer
