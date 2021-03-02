from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='agence_voyage-home'),
    path('Destinations/', views.about, name='agence_voyage-about'),
    path('Destinations/destination/', views.destination, name='agence_voyage-destination'),
    path('Destinations/voyage/', views.voyage, name='agence_voyage-voyage'),
    path('Excursions/', views.excursions, name='agence_voyage-excursions'),


]