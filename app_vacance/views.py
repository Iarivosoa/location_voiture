from django.shortcuts import render

def page_vacance(request):
    return render(request,"vacance.html")

# affiche la page voyage
def voyage(request):
    return render(request,"voyage.html")

# Create your views here.
