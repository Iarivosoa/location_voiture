from django.shortcuts import render,redirect
from .models import Insertion_membre
from django.core.exceptions import ValidationError
import hashlib
from django.core.validators import validate_email
from django.contrib.auth import logout
from django.contrib import messages
from django.views.decorators.cache import never_cache

# Create your views here.
def page_connexion(request):
    return render(request,"connexion.html")
def page_souscription(request):
    return render(request,"souscription.html")

# cryptage mot de passe
def crypt_mdp(mdp):
    crypt_mdps = hashlib.sha1()
    crypt_mdps.update(mdp.encode("utf-8"))
    return crypt_mdps.hexdigest()

# function pour souscrire des membres
@never_cache
def souscrire_membre(request):
    if request.session["client"]:
        return redirect("accueil")

    if request.method == "POST":
        
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        watsapp = request.POST.get("whatsapp")
        pays = request.POST.get("pays")

        if nom !="" and prenom != "" and email != "" and password != "" and confirm_password !="" and watsapp != "" and pays != "":
            try:
                validate_email(email)
            except ValidationError:
                erreur = "veuillez entrer un email validé"
                return render(request, "souscription.html", {"erreur": erreur})

            nombre_email = Insertion_membre.objects.filter(email = email)
            verification_email = len(nombre_email)
            if verification_email == 0:

                
                if confirm_password == password:
                    if watsapp.isdigit() and len(watsapp) >= 10:
                        Inserer = Insertion_membre.objects.create(
                                nom = nom,
                                prenom = prenom,
                                email = email,
                                passsword = crypt_mdp(password),
                                watsapp = watsapp,
                                pays = pays
                        )
                        Inserer.save()
                        messages.success(request,"Veuiller Connecter car votre compte a étet bien crée")
                        return redirect("page_connexion")
                    else:
                        erreur = "WatsApp non valide"
                        return render(request, "souscription.html", {"erreur": erreur}) 
                
                else:
                    erreur = "mot de passe non identique" 
                    return render(request, "souscription.html", {"erreur": erreur})          

            else:
                erreur = "Cet email est déjà utilisé, veuillez choisir un autre"
                return render(request, "souscription.html", {"erreur": erreur})
        else:
            erreur = "Veuillez remplir tous les champs."
            return render(request, "souscription.html", {"erreur": erreur})
        
    return render(request, "souscription.html")


# fonction connexion membre
@never_cache
def connexion_membre(request):
    if request.session["client"]:
        return redirect("accueil")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("mot_de_passe")
        validation = True

        if email !="" and password !="":

            
            recup_membre = Insertion_membre.objects.get(email=email)
            if not recup_membre:
                erreur = "Email non trouvé"
                return render(request,"connexion.html",{"erreur":erreur})
            
            if crypt_mdp(password) == recup_membre.passsword:
                validation = True
                pass
            else:
                erreur = "Mot de passe incrorrecte"
                return render(request,"connexion.html",{"erreur":erreur})
            if validation:
                recup_user = {
                    "id":recup_membre.id,
                    "nom":recup_membre.nom,
                    "email":recup_membre.email
                }
                request.session["client"] = recup_user

                return redirect("chargement")


        
        else:
            erreur = "Veuillez remplir tous les champs"
            return render(request,"connexion.html",{"erreur":erreur})


    return render(request,"connexion.html") 
# function de deconnexion

def deconnexion_membre(request):
    logout(request)
    return render(request,"chargement.html")
 

