from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("destinos", views.DestinoViewSet)
router.register("guias", views.GuiaViewSet)
router.register("tours", views.TourViewSet)
router.register("clientes", views.ClienteViewSet)
router.register("reservas", views.ReservaViewSet)

urlpatterns = [
    path("", views.bienvenida, name="bienvenida"),
    path("api/", include(router.urls)),
]
