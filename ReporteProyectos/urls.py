from django.urls import path
from ReporteProyectos.views import *

urlpatterns=[
    path("Resultados/",Resultados, name="resultados"),
    path("ListaProyectos/",ListaProyectos, name="ListaProyectos"),
    path("Reporte/<id>",Reportes,name="Reportes"),
    path("ListaProyectosCostos/",ListaProyectosCostos, name="ListaProyectosCostos"),
    
]