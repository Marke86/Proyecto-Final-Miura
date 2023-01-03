from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#------------------Forms para el registro/inicio--------------------------------------

class registroUsuarioForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="ingrese contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="repita contraseña", widget=forms.PasswordInput)  
    class Meta:

        model=User
        fields=["username","email","password1","password2"]
        help_texts = {k:"" for k in fields}
  
class usereditform(UserCreationForm):
    
    password1=forms.CharField(label="Ingrese contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repita contraseña", widget=forms.PasswordInput)
    email=forms.EmailField(label="Modificar Email")
    first_name=forms.CharField(label="Modificar Nombre")
    last_name=forms.CharField(label="Modificar Apellido")

    class Meta:
        model=User
        fields=["password1","password2","email","first_name","last_name"]
        help_texts = {k:"" for k in fields}
 
class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="imagen")

class MensajesForm(forms.Form):
    Mensaje=forms.CharField(max_length=300)

#-----------------Forms de la App----------------------------------------

class ProyectoForm(forms.Form):
    Nombre=forms.CharField(max_length=50)
    Codigo=forms.CharField(max_length=50)
    Presupuesto_Base=forms.IntegerField()

class DescripcionProyectoForm(forms.Form):    
    Descripcion=forms.CharField(max_length=1000)

class RegistrarReporteForm(forms.Form):
    Nombre_de_reporte=forms.CharField(label="Nombre de Reporte",max_length=50)
    Reporte=forms.CharField(max_length=1500)
    Imagen_Reporte=forms.ImageField(label="Imagen")