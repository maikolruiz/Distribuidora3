from django.shortcuts import render
from .models import links
from portafolio.models import Producto,category
from carro.carro import Carro


# Create your views here.

def home(request):
    projects=Producto.objects.all()
    categoria=category.objects.all()
    link=links.objects.all()
    carro = Carro(request)
    return render(request, 'core/home.html', {'projects':projects,'categoria':categoria,'link':link })

def about(request):
    link=links.objects.all()
    return render(request, 'core/about.html', {'link':link })

def contact(request):
    link=links.objects.all()
    return render(request, 'core/contact.html', {'link':link })

def product(request):
    categoria=category.objects.all()
    projects=Producto.objects.all()
    link=links.objects.all()
    return render(request, 'core/product.html', {'categoria':categoria,'projects':projects,'link':link })

def car(request):
    return render(request, "core/carrito.html")