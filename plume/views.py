from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from datetime import datetime
from django.utils import timezone
from .models import Legume

def home(request):
	legumes = Legume.objects.all()
	return render(request, 'Plume/Accueil.html', {'legumes': legumes})#, {'date': datetime.now()})
	
	
def catalogue(request):
	legumes = Legume.objects.all()
	return render(request, 'Plume/Catalogue.html', {'legumes': legumes})#, {'date': datetime.now()})
	
def lire(request, id):
    try:
        legume = Legume.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'Plume/lire.html', {'legume': legume})