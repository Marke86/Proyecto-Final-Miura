from django.shortcuts import render
from .models import *
from RegistroDeProyecto.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required #para vistas basdas en funciones


# Create your views here.
@login_required
def inicio(request):
    return render(request,"inicio.html", {"mensaje":"Página de inicio", "avatar":AvatarVER(request) })

@login_required
def AcercaDe(request):
    return render(request,"AcercaDe.html", {"mensaje":"Acerca de mí", "avatar":AvatarVER(request) })

#----------------------------------------------------------------------------
#-------------------Funciones de Registro------------------------------------
#----------------------------------------------------------------------------

def loginR(request):
    if request.method == "POST":
        form =AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")

            user=authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)                
                return render(request, "inicio.html", {"mensaje":f"Bienvenido/a {usuario}", "avatar":AvatarVER(request)})
            else:
                return render(request, "login.html", {"mensaje":"Error datos incorrectos", "form":form})

        else:
            return render(request, "login.html", {"mensaje":"Error formulario incorrectos", "form":form})

    form=AuthenticationForm()   
    return render(request, "login.html", {"form":form})

def register(request):
    if request.method=="POST":
        form=registroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
            return render(request, "inicio.html", {"mensaje":f"usuario {username} creado"})
        else:
            return render(request, "registro.html", {"form":form, "mensaje":"Error en la carga del formulario" } )
    else:
        form=registroUsuarioForm()
    return render(request,"registro.html", {"form":form})

@login_required
def editarperfil(request):
    usuario=request.user
   
    if request.method=="POST":
        form=usereditform(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save() 
            return render(request,"inicio.html",{"mensaje":"perfil modificado correctamente", "avatar":AvatarVER(request)})
        else:
            return render(request,"inicio.html",{"mensaje":"No se puedo modificar el perfil"})
    else:
        form=usereditform(instance=usuario)
        return render(request,"editperfil.html",{"form":form, "nombreusuario":usuario.username})

@login_required
def AgregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatarviejo=Avatar.objects.filter(user=request.user)
            if len(avatarviejo)!=0:
                avatarviejo[0].delete()
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatar.save()
            return render(request,"inicio.html",{"mensaje":"avatar agregado corectamente", "avatar":AvatarVER(request)})
    else:
        form=AvatarForm()
        return render(request, "AgregarAvatar.html", {"form":form, "usuario":request.user})

def AvatarVER(request):
    avatar=Avatar.objects.filter(user=request.user)
    if len(avatar)!=0:
        imagen=avatar[0].imagen.url
    else:
        imagen="/media/AvatarDefecto/avatarpordefecto.png"
    return imagen



#----------------------------------------------------------------------------------
#-------------------------Funciones de la APP--------------------------------------
#----------------------------------------------------------------------------------

@login_required
def ProyectoRegistro(request):
    if request.method == "POST":
        ProyFormulario=ProyectoForm(request.POST)
         
        if ProyFormulario.is_valid():
            info=ProyFormulario.cleaned_data
            NombreInfo=info["Nombre"]
            Codigoinfo=info["Codigo"]
            PresupuestoBaseInfo=info["Presupuesto_Base"]

            proyecto=Proyecto(Nombre=NombreInfo, Codigo=Codigoinfo, PresupuestoBase=PresupuestoBaseInfo)
            proyecto.save()
            return render(request, "inicio.html",{"mensaje":"El proyecto fue cargado con exito", "avatar":AvatarVER(request)})
    else:
        ProyFormulario=ProyectoForm()

    return render(request,"Proyecto_Registro.html",{"ProyFormulario":ProyFormulario})

@login_required
def AgregarDescripcion(request,id):
    proy=Proyecto.objects.get(id=id)
    if request.method=="POST":
        descripcion=DescripcionProyectoForm(request.POST) 

        if descripcion.is_valid():
            DescripcionCargada=DescripcionProy.objects.filter(Proyecto=proy)
            if len(DescripcionCargada)!=0:
                DescripcionCargada[0].delete()
            info=descripcion.cleaned_data
            descrip=DescripcionProy(Descripcion=info["Descripcion"],Proyecto=proy)            
            descrip.save()
            return render(request,"inicio.html",{"mensaje":"La descripción se ha cargado con éxito", "avatar":AvatarVER(request)})
    else:
        descripcion=DescripcionProyectoForm()
    return render(request,"Descripcion.html",{"descripcion":descripcion, "proy":proy})

@login_required
def ProyectosCargados(request):
    proyect=Proyecto.objects.all() #para traer todos los proyectos
    return render(request, "ProyectosAeditar.html", {"proyect":proyect,"nombretabla":"Proyectos cargados para editar","avatar":AvatarVER(request)})

@login_required
def EliminarProyecto(request, id):
    proy=Proyecto.objects.get(id=id)
    proy.delete()

    proyect=Proyecto.objects.all()
    return render(request, "VerProyectos.html", {"proyect":proyect, "avatar":AvatarVER(request)} )

@login_required
def AgregarReporte(request,id):
    proy=Proyecto.objects.get(id=id)
    if request.method=="POST":
        report=RegistrarReporteForm(request.POST, request.FILES)
        if report.is_valid():
            reportes=RegistrarReporte(Proyecto=proy,Nombredereporte=request.POST["Nombre_de_reporte"], reporte=request.POST["Reporte"], imagenReporte=request.FILES["Imagen_Reporte"])
            reportes.save()
            return render(request,"inicio.html",{"mensaje":"El reporte se ha cargado con exito", "avatar":AvatarVER(request)})

    else:
        formulario=RegistrarReporteForm()
    return render(request,"Registro_de_reporte.html",{"form":formulario, "proy":proy})

#=======================================================================================================
#=========================================FUNCIONES DE MENSAJES=========================================
#=======================================================================================================

@login_required
def ResultadoUsuario(request):
    if request.GET["first_name"]:
        Nombre=request.GET["first_name"]
        usuario=User.objects.filter(first_name__icontains=Nombre)

        return render(request,"ResultadoUsuario.html", {"usuario":usuario,"nombretabla":"Resultados de la busqueda", "avatar":AvatarVER(request)})
    else:
        return render(request, "inicio.html", {"mensaje":"No se han encontrado usuarios con el nombre indicado","avatar":AvatarVER(request)})

@login_required
def BuscarUsuario(request):
    return render(request, "BuscarUser.html")

@login_required
def EnviarMensaje(request, id):
    user=User.objects.get(id=id)
    if request.method=="POST":
        mensaje=MensajesForm(request.POST)
        if mensaje.is_valid():
            msj=Mensajes(User=user, MsjText=request.POST["Mensaje"])
            msj.save()
            return render(request,"inicio.html",{"mensaje":f"El mensaje se ha enviado a {user.first_name}", "avatar":AvatarVER(request)})

    else:
        mensaje=MensajesForm()
    return render(request,"EnviarMensaje.html",{"mensaje":mensaje, "user":user})

@login_required
def VerMensajes(request):
    MsjRec=Mensajes.objects.filter(User=request.user)
    if len(MsjRec)!=0:
        Mensaje="Se han encontrado los siguientes mensajes"
        Msj=MsjRec
    else:
        Msj="NO"
        Mensaje="No se han recibido mensajes"
    return render(request,"VerMensajes.html",{"Msj":Msj,"mensaje":Mensaje, "avatar":AvatarVER(request)})