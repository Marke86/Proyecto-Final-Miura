from django.shortcuts import render
from CostosProy.forms import *
from CostosProy.models import *
from RegistroDeProyecto.views import AvatarVER
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def ingenieria(request,id):
    proy=Proyecto.objects.get(id=id)
    valorHsIng=150
    if request.method=="POST":
        ing=IngForm(request.POST)

        if ing.is_valid():
            info=ing.cleaned_data
            NombreInfo=info["Nombre"]
            CodigoInfo=info["Codigo"]
            CantidadDOCInfo=info["Cantidad_DOC"]
            CantidaddeHsInfo=info["Cantidad_de_Hs"]
            CostoInfo=CantidaddeHsInfo*valorHsIng

            ingenieria=CostoIng(Proyecto=proy,Nombre=NombreInfo,Codigo=CodigoInfo,CantidadDOC=CantidadDOCInfo,CantidaddeHs=CantidaddeHsInfo,Costo=CostoInfo)
            ingenieria.save()

            return render(request,"inicio.html",{"mensaje":"La ingenieria fue caragada con exito", "avatar":AvatarVER(request)})

    else:
        IngFormulario=IngForm()
    
    return render(request,"RegistroIng.html",{"form":IngFormulario,"proy":proy})

@login_required
def montaje(request,id):
    proy=Proyecto.objects.get(id=id)
    if request.method=="POST":
        montaje=MontajeForm(request.POST)
        
        if montaje.is_valid():
            info=montaje.cleaned_data
            ContratistaInfo=info["Contratista"]
            MontoContratoInfo=info["Monto_Contrato"]
            Montaje=CostosMontaje(Proyecto=proy,Contratista=ContratistaInfo,MontoContrato=MontoContratoInfo)
            Montaje.save()

            return render(request,"inicio.html",{"mensaje":"El costo de montaje se ha cargado con exito", "avatar":AvatarVER(request)})

    else:
        MontajeFormulario=MontajeForm()

    return render(request, "RegistroMontaje.html", {"form":MontajeFormulario, "proy":proy})

@login_required
def materiales(request, id):
    proy=Proyecto.objects.get(id=id)
    if request.method=="POST":
        Mat=MaterialesForm(request.POST)

        if Mat.is_valid():
            info=Mat.cleaned_data
            CodigoInfo=info["Codigo"]
            NombreMatInfo=info["Nombre_Material"]
            CostoMatInfo=info["Costo_Material"]
            Material=Materiales(Proyecto=proy,Codigo=CodigoInfo,NombreMat=NombreMatInfo,CostoMat=CostoMatInfo)
            Material.save()

            return render(request,"inicio.html",{"mensaje":"El costo del material se ha cargado con exito", "avatar":AvatarVER(request)})

    else:
        MatFormulario=MaterialesForm()

    return render(request,"RegistroMateriales.html",{"form":MatFormulario, "proy":proy})
