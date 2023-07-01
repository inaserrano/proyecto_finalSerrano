from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm,TurnoForm
from django.contrib.auth import login,authenticate
from .models import Turno

def inicio(request):
    return render(request,"AppConsultorio/index.html")

def inicio_logeado(request):
    return render(request,"AppConsultorio/inicio.html")

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

@login_required
def solicitud_turno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'AppConsultorio/mostrar_turno.html')
    else:
        form = TurnoForm()
    return render(request, 'AppConsultorio/solicitud_turno.html', {'form': form})

def mas_info(request):
    turno = Turno.objects.latest('id')
    return render(request,"AppConsultorio/mas_info.html",{"turno":turno})

def mostrar_doctores(reuquest):
    pass

def registrar_doctor(request):
    pass

@login_required
def editar_perfil(request):
    pass