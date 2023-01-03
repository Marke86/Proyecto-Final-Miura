from django import forms

class IngForm(forms.Form):
    
    Nombre=forms.CharField(max_length=50)
    Codigo=forms.CharField(max_length=50)
    Cantidad_DOC=forms.IntegerField()
    Cantidad_de_Hs=forms.IntegerField()

class MontajeForm(forms.Form):
    Contratista=forms.CharField(max_length=50)
    Monto_Contrato=forms.IntegerField()

class MaterialesForm(forms.Form):
    Codigo=forms.CharField(max_length=50)
    Nombre_Material=forms.CharField(max_length=50)
    Costo_Material=forms.IntegerField()