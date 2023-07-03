from django import forms
from .models import Turno, Doctores
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2']
        help_texts = {k:"" for k in fields}

class TurnoForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(queryset=Doctores.objects.all())
    class Meta:
        model = Turno
        fields = ['nombre','apellido','email','dni','especialidad']
        
class DoctoresForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    apellido = forms.CharField(label='Apellido')
    num_licencia = forms.CharField(label='Número de Licencia')
    especialidad = forms.CharField(label='Especialidad')
    email = forms.EmailField(label='Email')
    dni = forms.CharField(label='DNI')
    
class SoliTurnoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    dni = forms.CharField(max_length=100)
    email = forms.EmailField()
    doctor = forms.ModelChoiceField(queryset=Doctores.objects.all())
    
class UserEditForm(UserCreationForm):
    email = forms.CharField(label="Ingrese su email:")
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña",widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
    class Meta:
        model = User
        fields = ['email','password1','password2','last_name','first_name']