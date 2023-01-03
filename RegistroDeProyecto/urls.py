from django.urls import path, include
from RegistroDeProyecto.views import *
from ReporteProyectos.views import Resultados, ListaProyectos, Reportes
from django.contrib.auth.views import LogoutView

urlpatterns=[
    path("inicio/",inicio, name="inicio"),
    path("ProyectoRegistro/",ProyectoRegistro,name="ProyectoRegistro"),
    path("Descripcion/<id>",AgregarDescripcion,name="descripcion"),
    path("Proyectos/",ProyectosCargados, name="proyectosCargados"),
    path("login/", loginR , name="login"),
    path("register/", register, name="register"),
    path("editarperfil/",editarperfil, name="editarperfil"),
    path("AgregarAvatar/",AgregarAvatar,name="AgregarAvatar"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('ReporteProyectos/',include('ReporteProyectos.urls')),
    path("Eliminarproyecto/<id>",EliminarProyecto, name="EliminarProyecto"),
    path("RegistrarReporte/<id>",AgregarReporte, name="AgregarReporte"),
    path("BuscarUsuario/",BuscarUsuario,name="BuscarUsuario"),
    path("ResultadoUsuario/", ResultadoUsuario, name="ResultadoUsuario"),
    path("EnviarMensaje/<id>",EnviarMensaje,name="EnviarMensaje"),
    path("Mensajes/",VerMensajes,name="VerMensajes"),
    path("AcercaDe/",AcercaDe,name="AcercaDe"),
]
