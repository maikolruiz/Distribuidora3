from django.shortcuts import render,redirect
from core.models import links
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

def contacto(request):
    contacto_formulario = ContactForm() #se instancia para enviarlo e un diccionario 
    if request.method == 'POST':
        contacto_formulario = ContactForm (data=request.POST)
        if contacto_formulario.is_valid():
            nombre = request.POST.get('nombre', '')
            correo = request.POST.get('correo', '')
            contenido = request.POST.get('contenido', '')
            correo = EmailMessage(
                "Distribuidora Conde's",
                "De {} <{}>\n\nEscribió:\n\n{}".format(nombre, correo,contenido),
                "stmp.gmail.com",
                ["sebasbonilla1706@gmail.com"],
                reply_to= [correo]
            )
            try:
                correo.send()
                # este el mensaje que envia en el caso de que todo se encuentre correctamente
                return redirect(reverse('contacto')+"?ok")
            except:
                #error que direcciona a un fallo
                return redirect(reverse('contacto')+"?fail")
        return redirect(reverse('contacto')+"?Enviado Correctamente")
    link=links.objects.all()
    return render (request, "contacto/contacto.html", {'link':link, 'form' : contacto_formulario })