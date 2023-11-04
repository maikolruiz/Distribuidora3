from django.urls import path

from .import views

app_name="carro"


urlpatterns = [

    path("agregar/<int:productos_id>/", views.agregar_producto, name="agregar"),
    path("eliminar/<int:productos_id>/", views.eliminar_producto, name="eliminar"),
    path("restar/<int:productos_id>/", views.restar_producto, name="restar"),
    path("limpiar/", views.limpiar_carro, name="limpiar"),

]