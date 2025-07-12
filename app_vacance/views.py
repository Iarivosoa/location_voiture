from django.shortcuts import render,redirect
from app_membre.models import Insertion_membre
from app_accueil.models import Insertion_voiture
from app_vacance.models import Site_park

def page_vacance(request):
    return render(request,"vacance.html")

# affiche la page voyage
def voyage(request):
    return render(request,"voyage.html")
# affiche tarif.html
def tarif(request):
    return render(request,"tarif.html")
# affiche reserveRapide.html
def rapide(request):
    return render(request,"reserveRapide.html")
# page afficher TOUS LES VOITURES pour une réservation
def tousVoiture(request):
    voitures = Insertion_voiture.objects.all()
    return render(request,"tousVoiture.html",{'tous_voiture':voitures})
# pour afficher le service rapide
def serviceRapide(request):
    return render(request,"serviceRapide.html")

# offre.html OFFRE DISPOS
def offre(request): 
    recup_offre = Site_park.objects.all()

    return render(request,"offre.html",{"Sites":recup_offre})

# Create your views here.
