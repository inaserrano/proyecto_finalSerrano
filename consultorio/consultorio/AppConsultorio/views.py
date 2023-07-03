from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm,TurnoForm,DoctoresForm
from django.contrib.auth import login,authenticate
from .models import Turno,Doctores
from .forms import UserEditForm

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
            return redirect(to='inicio_l')
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

@login_required
def mas_info(request):
    turno = Turno.objects.latest('id')
    return render(request,"AppConsultorio/mas_info.html",{"turno":turno})

@login_required
def registrar_doctor(request):
    if request.method == "POST":
        form = DoctoresForm(request.POST)
        if form.is_valid():
            doctores = Doctores(
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                num_licencia=form.cleaned_data['num_licencia'],
                especialidad=form.cleaned_data['especialidad'],
                email=form.cleaned_data['email'],
                dni=form.cleaned_data['dni'],
                doctor = form.cleaned_data['doctor']
            )
            
            doctores.save()
            return render(request, 'AppConsultorio/doctores.html')
    else:
        form = DoctoresForm()
        return render(request,'AppConsultorio/registrar_doctores.html',{"form":form})

@login_required 
def ver_doctores(request):
    doctores = Doctores.objects.all()
    return render(request, 'AppConsultorio/doctores.html',{'doctores':doctores})

@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        miFormulario = UserEditForm()
        if miFormulario.is_valid():
            info = miFormulario.cleaned_data()
            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.last_name = info['last_name']
            usuario.first_name = info['first_name']
            usuario.save()
            return render(request,"AppConsultorio/inicio_l.html")
    else:
        miFormulario = UserEditForm(initial ={'email':usuario.email})
    return render(request,"AppConsultorio/editar_perfil.html",{"miFormulario":miFormulario,"usuario":usuario})