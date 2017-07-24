from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
	universidades_lista = Ies.objects.all()
	cantidad_universidades = len(universidades_lista)
	carreras_lista = Carreras.objects.all()
	cantidad_carreras = len(carreras_lista)
	areas_lista = Areas.objects.all()
	cantidad_areas = len(areas_lista)
	universidades_lista = Ies.objects.all()
	cantidad_universidades = len(universidades_lista)
	return render(request, 'index.html', {'cantidad_universidades':cantidad_universidades, 'cantidad_carreras':cantidad_carreras, 'cantidad_areas':cantidad_areas})

def estadisticas(request):
	area = Areas.objects.all()
	return render(request, 'estadisticas.html', {'area':area})

def universidades(request):
	if request.GET.get('buscar_universidad') is not None:
		nombre_universidad = request.GET.get('buscar_universidad')
		universidades_lista = Ies.objects.filter(nombre__icontains=nombre_universidad)
	else:
		universidades_lista = Ies.objects.all()

	paginator = Paginator(universidades_lista, 12) #U por pagina
	page = request.GET.get('page')
	try:
		universidades = paginator.page(page)
	except PageNotAnInteger:
		universidades = paginator.page(1)
	except EmptyPage:
		universidades = paginator.page(paginator.num_pages)

	buscar_universidad = request.GET.get('buscar_universidad')
	cantidad_universidades = len(universidades_lista)

	return render(request, 'universidades.html', {'universidades':universidades, 'buscar_universidad':buscar_universidad, 'cantidad_universidades':cantidad_universidades})

def universidad(request):
	id = request.GET.get('id')
	institucion = Ies.objects.get(pk=id)
	matriz = Matriz.objects.get(id_ies=id)
	listado_carreras = IesCarreras.objects.filter(id_ies=id)
	try:
		sede = Sede.objects.get(id_ies=id)
		extension = Extension.objects.get(id_ies=id)
		return render(request, 'universidad.html', {'institucion':institucion, 'matriz':matriz, 'listado_carreras':listado_carreras, 'sede':sede, 'extension':extension})
	except ObjectDoesNotExist:
		sede = 0
		extension = 0
		return render(request, 'universidad.html', {'institucion':institucion, 'matriz':matriz, 'listado_carreras':listado_carreras})


	