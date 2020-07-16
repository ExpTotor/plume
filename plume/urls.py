from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home),
	path('catalogue', views.catalogue),
	path('article/<int:id>', views.lire, name='lire')
]