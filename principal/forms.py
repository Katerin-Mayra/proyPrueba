from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from principal.models import Profile

class FormPerfil(forms.ModelForm):
    class Meta:
        model = Profile 

        fields = [
            'ci', 
            'name',
            'last_name',
            'email',
            'phone',
            'whatsapp',
            'image',
        ]
        labels = {
            'ci': 'C.I.',
            'name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
            'phone': 'Telefono',
            'whatsapp': 'Whatsapp',
            'image': 'Imagen',
        }
        widgets = {
            'ci': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.TextInput(attrs={'class': 'form-control'}),
        }

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'is_superuser',
        ]
        labels = {
            'username': 'Nombre de Usuario',
            'email': 'Correo',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'password1': 'Contraseña',
            'password2': 'Confirmar Contraseña',
            'is_superuser': 'Administrador',
        }


"""
class FormPerfilUpdate(forms.Form):
    name = forms.CharField(
        label = "Nombre"
    )
    last_name = forms.CharField(
        label = "Apellido"
    )
    email = forms.CharField(
        label = "Correo"
    )
    phone = forms.CharField(
        label = "Telefono"
    )
    whatsapp = forms.CharField(
        label = "Whatsapp"
    )
    image = forms.CharField(
        label = "Subir imagen"
    )




    class FormPerfil(forms.Form):
        CI = forms.CharField(
        label = "C.I."
        )
        name = forms.CharField(
            label = "Nombre"
        )
        last_name = forms.CharField(
            label = "Apellido"
        )
        email = forms.CharField(
            label = "Correo"
        )
        phone = forms.CharField(
            label = "Telefono"
        )
        whatsapp = forms.CharField(
            label = "Whatsapp"
        )
        image = forms.CharField(
            label = "Subir imagen"
        )
"""