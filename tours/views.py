from django.http import HttpResponse
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
    return HttpResponse(
        "<h1>API de Viajes y Turismo</h1>"
        "<p>Bienvenido a la plataforma de gestión de tours y reservas.</p>"
    )


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
