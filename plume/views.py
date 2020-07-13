from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.utils import timezone
from .models import Legume

def home(request):
	legumes = Legume.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'Plume/Accueil.html', {'date': datetime.now()}, {'legumes': legumes})
	