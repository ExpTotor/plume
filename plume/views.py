from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.utils import timezone
from .models import Legume

def home(request):
	legumes = Legume.objects.all()
	return render(request, 'plume/Accueil.html', {'legumes': legumes})#, {'date': datetime.now()})
	
	
def catalogue(request):
	legumes = Legume.objects.all()
	return render(request, 'plume/Catalogue.html', {'legumes': legumes})#, {'date': datetime.now()})