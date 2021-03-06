from django import forms
from django.contrib.auth.models import User
from .models import *

class DestinationForm(forms.Form):
    pays=forms.CharField(label='Pays',required=True,
        error_messages={'required':'cette champ ne peut etre vide !!'},
        widget=forms.TextInput(
            attrs={ "class":"form-control"}
        )
    )
class CreatVoyage(forms.Form):
    nom = forms.CharField(label='Nom Voyage',required=True,
        error_messages={'required':'cette champ ne peut etre vide !'},
        widget=forms.TextInput(
            attrs={ "class":"form-control"}
        ))
    photo = forms.ImageField()
    duree = forms.IntegerField(label='Duree(en heure)',required=True,
        error_messages={'required':'cette champ ne peut etre vide !!!'},
        widget=forms.NumberInput(
            attrs={ "class":"form-control"}
        ))
    prix = forms.FloatField(label='Montant',required=True,
        error_messages={'required':'cette champ ne peut etre vide !!!'},
        widget=forms.NumberInput(
            attrs={ "class":"form-control"}
        ))
    destination= forms.ModelChoiceField(
    queryset=Destination.objects.all()
       
    )
    excursion= forms.ModelMultipleChoiceField(
    queryset=Excursion.objects.all()
    )