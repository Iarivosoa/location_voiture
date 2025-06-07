from django.shortcuts import render

# Create your views here.
def page_connexion(request):
    return render(request,"connexion.html")
def page_souscription(request):
    return render(request,"souscription.html")