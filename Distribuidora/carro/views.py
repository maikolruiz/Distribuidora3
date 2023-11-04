from django.shortcuts import render

from .carro import Carro

from portafolio.models import Producto

from django.shortcuts import redirect

# Create your views here.

def agregar_producto(request, productos_id):

    carro = Carro(request)

    producto = Producto.objects.get(id=productos_id)

    carro.agregar(productos=producto)

    return redirect("car")

def eliminar_producto(request, productos_id):

    carro = Carro(request)

    producto = Producto.objects.get(id=productos_id)

    carro.eliminar(productos=producto)

    return redirect("car")

def restar_producto(request, productos_id):

    carro = Carro(request)

    producto = Producto.objects.get(id=productos_id)

    carro.restar_producto(productos=producto)

    return redirect("car")

def limpiar_carro(request):

    carro = Carro(request)

    carro.limpiar_carro()

    return redirect("car")