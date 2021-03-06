from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='agence_voyage-accueil'),
    path('Destinations/', views.destinations, name='agence_voyage-destinations'),
    path('Destinations/voyage/<int:id>', views.destination, name='agence_voyage-destination'),
    path('Excursions/voyage/<int:id>', views.voyage, name='agence_voyage-voyage'),
    path('Excursions/', views.excursions, name='agence_voyage-excursions'),

    path('AjouterDestination/', views.destinationform, name='agence_voyage-dest_form'),
    path('AjouterVoyage/', views.createVoyage, name='agence_voyage-voyage_form'),

    


]