from django.shortcuts import render
from RegistroDeProyecto.models import *
from RegistroDeProyecto.forms import *
from CostosProy.models import *
from CostosProy.forms import *
from django.contrib.auth.decorators import login_required
from RegistroDeProyecto.views import *


# Create your views here.

@login_required
def ListaProyectos(request):
    proyect=Proyecto.objects.all() #para traer todos los proyectos
    descrip=DescripcionProy.objects.all()
    
    return render(request, "VerProyectos.html", {"proyect":proyect,"descrip":descrip,"mensaje":"Lista de Proyectos","tituloprincipal":"PROYECTOS", "avatar":AvatarVER(request)})

@login_required
def Resultados(request):

    if request.GET["Nombre"]:   

        Nombre=request.GET["Nombre"]

        proyect=Proyecto.objects.filter(Nombre__icontains=Nombre)
            
        return render(request,"Resultados.html", {"proyect":proyect,"nombretabla":"Resultados de la busqueda", "avatar":AvatarVER(request)} )
    else:
        return render(request, "inicio.html", {"mensaje":"No se han encontrado coincidencias", "avatar":AvatarVER(request)})

@login_required
def Reportes(request, id):
    proy=Proyecto.objects.get(id=id)

    Nombre=proy.Nombre  
    Presupuesto=proy.PresupuestoBase

    CHEKdescrip=DescripcionProy.objects.filter(Proyecto=proy)
    if len(CHEKdescrip)!=0:
        descrip=DescripcionProy.objects.get(Proyecto=proy)
        Descripcion=descrip.Descripcion
    else:
        Descripcion="Agregar descripción"
    
    CHEKcostoING=CostoIng.objects.filter(Proyecto=proy)
    if len(CHEKcostoING)!=0:
        costoING=CostoIng.objects.get(Proyecto=proy)
        Ing=costoING.Costo
    else:
        Ing=0

    CHEKcostoMontaje=CostosMontaje.objects.filter(Proyecto=proy)
    if len(CHEKcostoMontaje)!=0:
        costoMontaje=CostosMontaje.objects.get(Proyecto=proy)
        Montaje=costoMontaje.MontoContrato
    else:
        Montaje=0

    CHEKcostoMateriales=Materiales.objects.filter(Proyecto=proy)
    if len(CHEKcostoMateriales)!=0:
        costoMateriales=Materiales.objects.filter(Proyecto=proy)
        costot=0
        for C in costoMateriales:
            Costo=C.CostoMat
            costot=costot+Costo
    else:
        costot=0

    reportes=RegistrarReporte.objects.filter(Proyecto=proy)

    
    return render(request,"Reporte.html",{"nombretabla":"Reportes del Proyecto","nombre":Nombre,"titulo":"Descripción", "mensaje":Descripcion,"PresupuestoBase":Presupuesto, "CostoIng":Ing, "CostoMontaje":Montaje, "CostoMateriales":costot, "reportes":reportes, "avatar":AvatarVER(request)})

@login_required
def ListaProyectosCostos(request):
    proyect=Proyecto.objects.all() #para traer todos los proyectos
    
    
    return render(request, "Lista_Costo_proyectos.html", {"proyect":proyect,"nombretabla":"Proyectos para incluir costos", "avatar":AvatarVER(request)})













