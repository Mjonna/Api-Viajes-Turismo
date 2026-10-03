from django.db import models


class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=60)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.pais})"


class Guia(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nombre


class Tour(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_dias = models.PositiveIntegerField()
    cupos = models.PositiveIntegerField()
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE, related_name="tours")
    guia = models.ForeignKey(
        Guia, on_delete=models.SET_NULL, null=True, blank=True, related_name="tours"
    )

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    ESTADOS = [
        ("pendiente", "Pendiente"),
        ("confirmada", "Confirmada"),
        ("cancelada", "Cancelada"),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="reservas")
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="reservas")
    fecha_reserva = models.DateField(auto_now_add=True)
    cantidad_personas = models.PositiveIntegerField(default=1)
    estado = models.CharField(max_length=12, choices=ESTADOS, default="pendiente")

    def __str__(self):
        return f"Reserva {self.id} - {self.cliente} - {self.tour}"
