from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    imagen=models.ImageField(upload_to="Avatares")
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.imagen}"

class Mensajes(models.Model):
    MsjText=models.CharField(max_length=300)
    User=models.ForeignKey(User, on_delete=models.CASCADE)
    



class Proyecto(models.Model):
    Nombre=models.CharField(max_length=50)
    Codigo=models.CharField(max_length=50)
    PresupuestoBase=models.IntegerField()

    def __str__(self):
        return self.Nombre

class DescripcionProy(models.Model):    
    Descripcion=models.CharField(max_length=1000, default="Agregar un valor")
    Proyecto=models.OneToOneField(Proyecto, on_delete=models.CASCADE)

class RegistrarReporte(models.Model):
    Proyecto=models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    Nombredereporte=models.CharField(max_length=50)
    reporte=models.CharField(max_length=1500)
    imagenReporte=models.ImageField(upload_to="IMGReporte")