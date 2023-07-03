from django.urls import path
from AppConsultorio import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('registro/',views.registro_usuario,name='registro_usuario'),
    path('solicitud_turno/',views.solicitud_turno,name="solicitud_turno"),
    path('mas_info/',views.mas_info, name="info"),
    path('inicio_l/',views.inicio_logeado,name='inicio_l'),
    path('registrar_doctor/',views.registrar_doctor,name='registrar_doctor'),
    path('ver_doctores/',views.ver_doctores,name="ver_doctores"),
    path('editar_perfil/',views.editar_perfil,name='editar_perfil'),

]