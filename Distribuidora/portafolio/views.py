from django.shortcuts import render
from .models import Producto
from core.models import links

# Create your views here.

def portafolio(request):
    projects=Producto.objects.all()
    link=links.objects.all()
    return render (request, "portafolio/portafolio.html",{'projects':projects,'link':link})
