from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm
from django.contrib.auth import login,authenticate

def inicio(request):
    return render(request,"AppConsultorio/index.html")


def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect(to='inicio')
    return render(request,"registration/registrar.html",data)

# @login_required
def solicitar_turno(request):
    pass

def mostrar_doctores(reuquest):
    pass

def registrar_doctor(request):
    pass