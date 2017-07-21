from django.contrib import admin
from .models import *

modelos = [Areas, Carreras, CarrerasModalidad ,Catalogo, DetalleCatalogo, Extension, Ies, IesCarreras, Matriculados, Matriz, Modalidad, NivelFormacion, Sede, Titulados]
admin.site.register(modelos)
# admin.site.register(Carreras)
# admin.site.register(Catalogo)
# admin.site.register(DetalleCatalogo)
# admin.site.register(Ies)
# admin.site.register(NivelFormacion)