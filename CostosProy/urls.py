from django.urls import path
from CostosProy.views import *

urlpatterns=[path("Costoing/<id>",ingenieria,name="costoing"),
            path("CostoMontaje/<id>",montaje,name="costomontaje"),
            path("CostoMateriales/<id>",materiales,name="costomateriales")

]