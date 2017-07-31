from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.db.models import Count
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
	matriculados_lista = Matriculados.objects.all()
	cantidad_matriculados = len(matriculados_lista)
	universidades_random= Ies.objects.order_by('?')[:5]
	return render(request, 'index.html', {'cantidad_universidades':cantidad_universidades, 'cantidad_carreras':cantidad_carreras, 'cantidad_areas':cantidad_areas, 'cantidad_matriculados':cantidad_matriculados, 'universidades_random':universidades_random})

def estadisticas(request):
	area = Areas.objects.all()
	return render(request, 'estadisticas.html', {'area':area})

def universidades(request):
	if request.GET.get('buscar_universidad') is not None:
		nombre_universidad = request.GET.get('buscar_universidad')
		universidades_lista = Ies.objects.filter(nombre__icontains=nombre_universidad) or Ies.objects.filter(acronimo__icontains=nombre_universidad)
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
	matriz = Matriz.objects.filter(id_ies=id)
	listado_carreras = IesCarreras.objects.filter(id_ies=id)
	try:
		sede = Sede.objects.filter(id_ies=id)
		extension = Extension.objects.filter(id_ies=id)
		return render(request, 'universidad.html', {'institucion':institucion, 'matriz':matriz, 'listado_carreras':listado_carreras, 'sede':sede, 'extension':extension})
	except ObjectDoesNotExist:
		return render(request, 'universidad.html', {'institucion':institucion, 'matriz':matriz, 'listado_carreras':listado_carreras})

def mapa(request):
	matriz = Matriz.objects.all()
	sede = Sede.objects.all()
	extension = Extension.objects.all()

	return render(request, 'mapa.html', {'matriz':matriz, 'sede':sede, 'extension':extension})

def mapa_titulados(request):
	titulados = Titulados.objects.all()

	return render(request, 'mapa_titulados.html', {'titulados':titulados})

def titulados(request):
	titulados = Titulados.objects.all()

	return render(request, 'titulados.html', {'titulados':titulados})

def matriculados(request):

	if request.GET.get('u1') is not None and request.GET.get('u2') is not None:
		u1 = request.GET.get('u1')
		u2 = request.GET.get('u2')
		m1 = Matriculados.objects.filter(id_ies=u1)
		m2 = Matriculados.objects.filter(id_ies=u2)
	else:
		m1 = None
		m2 = None

	# llenar select
	matriculados = Matriculados.objects.all()

	return render(request, 'matriculados.html', {'matriculados':matriculados, 'm1':m1, 'm2':m2})

def graficos_u(request):
	categorias = Ies.objects.values('categoria').annotate(dcount=Count('categoria'))
	tipos = Ies.objects.values('tipo').annotate(dcount=Count('tipo'))
	carrera = Carreras.objects.all()
	carreras = Carreras.objects.values('id_area').annotate(dcount=Count('id_area'))

	return render(request, 'graficos_u.html', {'categorias':categorias, 'tipos':tipos, 'carreras':carreras, 'carrera':carrera})
	
def docentes(request):

	if request.GET.get('u1') is not None and request.GET.get('u2') is not None:
		u1 = request.GET.get('u1')
		u2 = request.GET.get('u2')
		universidad1 = Ies.objects.filter(id_ies=u1)
		universidad2 = Ies.objects.filter(id_ies=u2)
	else:
		universidad1 = None
		universidad2 = None

	# llenar select
	ies = Ies.objects.all()

	return render(request, 'docentes.html', {'ies':ies, 'universidad1':universidad1, 'universidad2':universidad2})