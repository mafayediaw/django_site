from agent_voyage.forms import DestinationForm, CreatVoyage
from django.shortcuts import get_object_or_404, render
from django .http import HttpResponse
from agent_voyage.models import Destination
from agent_voyage.models import Voyage
from agent_voyage.models import Excursion


def accueil(request):

    return render(request, 'voyage/accueil.html')


def destinations(request):
    context = {
        'destinations': Destination.objects.all(),
        'voyages': Voyage.objects.all()
    }
    return render(request, 'voyage/destinations.html', context)


def destination(request, id):
    context = {'destId': get_object_or_404(Voyage, id=id)
               }
    return render(request, 'voyage/destination.html', context)


def voyage(request, id):
    context = {
        'excursionId': get_object_or_404(Voyage, id=id)
    }
    return render(request, 'voyage/voyage.html', context)


def excursions(request):

    v = Voyage.objects.all()
    context = {
        'voyage': v}
    return render(request, 'voyage/excursions.html', context)


def destinationform(request):
    sauvegarde = False
    dest_form = DestinationForm(request.POST or None)
    if dest_form.is_valid():
        pays = dest_form.cleaned_data.get('pays')
        destination = Destination(pays=pays)
        destination.save()
        sauvegarde = True
    else:
        dest_form = DestinationForm()
    context = {
        'dest_form': dest_form,
        'statut': sauvegarde

    }
    return render(request, 'voyage/destination_form.html', context)


def createVoyage(request):
    sauvegarde = False
    voyage_form = CreatVoyage(request.POST)
    if voyage_form.is_valid():
        voyage = Voyage()
        voyage.nom = voyage_form.cleaned_data["nom"]
        voyage.photo = voyage_form.cleaned_data["photo"]
        voyage.duree = voyage_form.cleaned_data["duree"]
        voyage.prix = voyage_form.cleaned_data["prix"]
        voyage.destination = voyage_form.cleaned_data["destination"]
        voyage.excursion = voyage_form.cleaned_data["excursion"]
        print(voyage.nom)

        voyage.save()
        sauvegarde = True
    else:
        voyage_form = CreatVoyage()
    
    context = {
        'status': sauvegarde,
        'voyage_form': voyage_form
    }

    return render(request, 'voyage/voyage_form.html', context)
