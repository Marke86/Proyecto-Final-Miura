from django.db import models
from RegistroDeProyecto.models import Proyecto

# Create your models here.

class CostoIng(models.Model):

    Proyecto=models.OneToOneField(Proyecto, on_delete=models.CASCADE, primary_key=True)
    Nombre=models.CharField(max_length=50)
    Codigo=models.CharField(max_length=50)
    CantidadDOC=models.IntegerField()
    CantidaddeHs=models.IntegerField()
    Costo=models.IntegerField()


    def __str__(self):
        return f"codiigo: {self.Codigo} Nombre: {self.Nombre}"


class CostosMontaje(models.Model):
    Proyecto=models.OneToOneField(Proyecto, on_delete=models.CASCADE, primary_key=True)
    Contratista=models.CharField(max_length=50)
    MontoContrato=models.IntegerField()
    def __str__(self):
        return f"Contratista: {self.Contratista} Monto: {self.MontoContrato}"



class Materiales(models.Model):

    Proyecto=models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    Codigo=models.CharField(max_length=50)
    NombreMat=models.CharField(max_length=50)
    CostoMat=models.IntegerField()
 
    def __str__(self):
        return f"codiigo: {self.Codigo} Nombre: {self.NombreMat} Costo:{self.CostoMat}"

