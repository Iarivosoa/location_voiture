from django.shortcuts import render,redirect
from .models import Insertion_membre
from django.core.exceptions import ValidationError
import hashlib
from django.core.validators import validate_email
from django.contrib.auth import logout
from django.contrib import messages
from django.core.mail import send_mail
from django.views.decorators.cache import never_cache
from django.conf import settings
from datetime import datetime
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required

# Create your views here.
def page_connexion(request):
    if request.session.get("client"):
        return redirect("accueil")
    return render(request,"connexion.html")
def page_souscription(request):
    if request.session.get("client"):
        return redirect("accueil")
    return render(request,"souscription.html")

# cryptage mot de passe
def crypt_mdp(mdp):
    crypt_mdps = hashlib.sha1()
    crypt_mdps.update(mdp.encode("utf-8"))
    return crypt_mdps.hexdigest()

# function pour souscrire des membres
@never_cache
def souscrire_membre(request):
    if request.session.get("client"):
        return redirect("accueilz")
 
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
    if request.session.get("client"):
        return redirect("accueil")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("mot_de_passe")
        validation = True
        try:

            if email !="" and password !="":
                recup_membre = Insertion_membre.objects.get(email = email)
                if crypt_mdp(password) != recup_membre.passsword:
                    validation = False
                    erreur = "Mot de passe incrorrecte"
                    return render(request,"connexion.html",{"erreur":erreur})

                if recup_membre.email == email :
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
        except Insertion_membre.DoesNotExist:
            validation = False
            erreur = "compte n'existe pas"
            return render(request,"connexion.html",{"erreur":erreur})
                



    return render(request,"connexion.html") 
# function de deconnexion

def deconnexion_membre(request):
    logout(request)
    return render(request,"chargement.html")
 
# reset mot de passe
def reset_password(request):
    if request.method == "POST":
        email_reset = request.POST.get("email_reset")

        recup_email = Insertion_membre.objects.get(email = email_reset)
        try:
            token = get_random_string(length=32)
            recup_email.reset_token = token

            recup_email.reset_token_created = datetime.now()
            recup_email.save()

            # envoie lien vers email
            lien_reset = f"{request.scheme}://{request.get_host()}/reset_password/{token}"
            send_mail(
                "REINITIALISATION DE VOTRE MOT DE PASSE",
                f"Cliquer sur ce lien ci_dessous pour réinitialier votre mot de passe :\n {lien_reset} \n ce lien sera expiré dans 1 heure",
                settings.EMAIL_HOST_USER,
                [email_reset],
                fail_silently=False
            )
        except Insertion_membre.DoesNotExist:
            return render(request,"reset_password.html",{"message":"Cet email n'existe pas"})
    return render(request,"reset_password.html",{"message":"Consulter votre email pour avoir le lien"})
# pager pour le nouveau mot de passe
def page_reset_password(request, token):

    if request.method == "POST":
        new_password = request.POST.get("new_password")
        confirm_new_password = request.POST.get("confirm_password")

        if new_password and confirm_new_password:
            if new_password == confirm_new_password:
                try:
                    recup_email = Insertion_membre.objects.get(reset_token=token)
                    token_delais = timezone.now()- recup_email.reset_token_created
                    if token_delais.total_seconds() > 3600:  # 1 heure en secondes
                        return render(request, "page_reset.html", {"message": "Le lien a expiré. Veuillez demander une nouvelle réinitialisation."})
                    recup_email.passsword = crypt_mdp(new_password)
                    recup_email.reset_token = None
                    recup_email.reset_token_created = None
                    recup_email.save()
                    messages.success(request, "Votre mot de passe a été réinitialisé avec succès.")
                    return redirect("page_connexion")
                except Insertion_membre.DoesNotExist:
                    return render(request, "page_reset.html", {"message": "Lien invalide ou expiré."})
            else:
                return render(request, "page_reset.html", {"message": "Les mots de passe ne correspondent pas."})
        else:
            return render(request, "page_reset.html", {"message": "Veuillez remplir tous les champs."})

    return render(request, "page_reset.html")