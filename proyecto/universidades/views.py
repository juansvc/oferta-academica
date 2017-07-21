from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
	return render_to_response('index.html', context=RequestContext(request))

def estadisticas(request):
	return render_to_response('estadisticas.html', context=RequestContext(request))
