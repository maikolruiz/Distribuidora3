from .forms import UserCreationFormWithEmail
from django import forms
from django.views.generic import CreateView
from django.urls import  reverse_lazy





# Create your views here.

 

#-----------------------------------------------------------------------------------------------------------------------------------

class SignUpView(CreateView): #registro usuario
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'
    #success_url = reverse_lazy('login') + '?register' 

    def get_success_url(self):
        return reverse_lazy('login') + '?register'   
        

    def get_form(self, form_class=None):
        form  = super (SignUpView, self).get_form()
        form.fields['email'].widget = forms.EmailInput ( attrs={'class':'form-control mb-2', 'placeholder':'Direccion email'})
        form.fields['username'].widget = forms.TextInput( attrs={'class': 'form-control mb-2', "placeholder": 'Nombre de usuario'})
        form.fields['password1'].widget = forms.PasswordInput (attrs={'class':'form-control mb-2', "placeholder": 'Contraseña'}) 
        form.fields['password2'].widget = forms.PasswordInput (attrs={'class':'form-control mb-2', "placeholder": 'Repita la contraseña'})
        form.fields['username'].label = ''
        form.fields['email'].label = ''
        form.fields['password1'].label = ''
        form.fields['password2'].label = ''
        return form
    
    def form_valid(self, form):
        # Valida el CAPTCHA junto con el formulario
        if form.is_valid():
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

