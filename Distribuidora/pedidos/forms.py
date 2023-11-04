from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    ciudad = forms.CharField(
        label="Ciudad",
        widget=forms.TextInput(attrs={'placeholder': 'Escriba su ciudad', 'class': 'form-control'}),
        required=True,
        max_length=100  # Ajusta la longitud máxima según tus necesidades
    )
    
    direccion = forms.CharField(
        label="Dirección",
        widget=forms.TextInput(attrs={'placeholder': 'Escriba su dirección', 'class': 'form-control'}),
        required=True,
        max_length=255  # Ajusta la longitud máxima según tus necesidades
    )
    
    telefono = forms.CharField(
        label="Teléfono",
        widget=forms.TextInput(attrs={'placeholder': 'Escriba su teléfono', 'class': 'form-control'}),
        required=True,
        max_length=15  # Ajusta la longitud máxima según tus necesidades
    )

    class Meta:
        model = UserProfile
        fields = ['ciudad', 'direccion', 'telefono']