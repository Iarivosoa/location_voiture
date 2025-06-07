from django.shortcuts import render
from .models import Insertion_voiture
from django.core.paginator import Paginator
from .views import*

# Create your views here.
def affiche_index(request):
    recup_prod = Insertion_voiture.objects.all()
    pagination = Paginator(recup_prod,6)
    page_num = request.GET.get("page",1)

    recup_type = set(article.types for article in recup_prod)

    try:
        page = pagination.page(page_num)
    except:
        page = pagination.page(1)
    
    contenu = {
        "produit":page,
        "tous_prod":recup_prod,
        "types":recup_type
    }

    return render(request,"index.html",contenu)
# detail des voitures
def detail(request,id):
    recup_detail = Insertion_voiture.objects.get(pk = id)
    return render(request,"detail.html",{"detail":recup_detail})
#page de chargement
def chargement(request):
    return render(request,"chargement.html")
#recuperation taxi
def recup_taxi(request):
    taxis = Insertion_voiture.objects.filter(type__icontains="taxi")
    return render(request,"index.html",{"taxis":taxis})

#afficher la page service
def service(request):
    return render(request,'service.html')

#afficher la page offre
def offre(request):
    return render(request,'offre.html')