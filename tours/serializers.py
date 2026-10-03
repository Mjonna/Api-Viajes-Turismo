from rest_framework import serializers

from .models import Destino, Guia, Tour, Cliente, Reserva


class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = "__all__"


class GuiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guia
        fields = "__all__"


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = "__all__"


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = "__all__"
