from django.shortcuts import render, redirect
from .models import Reservation
from app_membre.models import Insertion_membre
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
import random, string
from django.conf import settings
import os


# Create your views here.
def res(request,id):
    return render(request, 'reservation.html', {'id': id})

def reservation(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        telephone = request.POST.get('telephone')
        ville_depart = request.POST.get('destination')
        compagnie_vol = request.POST.get('compagnie_vol')
        date_depart = request.POST.get('date_depart')
        nombre_personnes = request.POST.get('nombre_personnes')
        bagages = request.POST.get('bagages') == 'True'
        commentaire = request.POST.get('commentaire')
        destination = request.POST.get('destination')

        # Création ou récupération du client (Insertion_membre)
        # Générer un numéro de réservation unique
        id_membre = request.session["client"]["id"]

        client = Insertion_membre.objects.filter(id=id_membre).first()

        numero_reservation = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        while Reservation.objects.filter(numero_reservation=numero_reservation).exists():
            numero_reservation = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

        reservation_obj = Reservation.objects.create(
            client=nom,
            destination=destination,
            ville_depart=ville_depart,
            compagnie_vol=compagnie_vol,
            date_depart=date_depart,
            nombre_personnes=nombre_personnes,
            bagages=bagages,
            commentaire=commentaire,
            numero_reservation=numero_reservation,
            telephone=telephone,
            email_client=client.email if client else None,
        )
        # Envoi d'un email de confirmation si l'email du client existe
        
        
        send_mail(
            'Confirmation de votre réservation de taxi auprès de TAXI EXPRESS avec le Teams Express',
            f'Bonjour {client.prenom},\n\nVotre réservation a bien été enregistrée.\nNuméro de réservation : {numero_reservation}\nDépart : {ville_depart}\nCompagnie de vol : {compagnie_vol}\nDate et heure : {date_depart}\n\nMerci d\'avoir choisi notre service !',
            settings.EMAIL_HOST_USER ,
            [client.email,"fify.dev1706@gmail.com"],
            fail_silently=True,
        )
        messages.success(request, f"Votre réservation a bien été enregistrée ! Numéro : {numero_reservation}")
        return redirect('reservation', id=reservation_obj.id)

    return render(request, 'reservation.html')

# utilisation de twilio pour envoyer un sms de confirmation
# def envoyer_whatsapp(request):

#     from twilio.rest import Client

#     if request.method == "POST":



#         nom = request.POST.get("contact_nom")
#         whatsapp_client = request.POST.get("contact_whatsapp")
#         message = request.POST.get("contact_message")

#         sid = os.getenv('TWILIO_ACCOUNT_SID')
#         token = os.getenv('TWILIO_AUTH_TOKEN')
#         client = Client(sid,token)
        
#         message = client.messages.create(
#                 body=message,
#                 from_='whatsapp:+14155238886',  # Numéro WhatsApp de Twilio
#                 to=f'whatsapp:+{whatsapp_client}'  # Numéro WhatsApp du client
#             )
#         messages.success(request, "Message envoyé avec succès !")

#         messages.error(request, "Veuillez remplir tous les champs.")
#         return redirect("serviceRapide")

    # fonction pour la reservation rapide
   
# VERSION 2
import os
from django.contrib import messages
from django.shortcuts import redirect
from twilio.rest import Client
from dotenv import load_dotenv

# Charger .env
load_dotenv()

def envoyer_whatsapp(request):
    if request.method == "POST":
        nom = request.POST.get("contact_nom")
        whatsapp_client = request.POST.get("contact_whatsapp")
        message_text = request.POST.get("contact_message")

        if not nom or not whatsapp_client or not message_text:
            messages.error(request, "Veuillez remplir tous les champs.")
            return redirect("serviceRapide")

        sid = os.getenv('TWILIO_ACCOUNT_SID')
        token = os.getenv('TWILIO_AUTH_TOKEN')

        if not sid or not token:
            messages.error(request, "Identifiants Twilio manquants.")
            return redirect("serviceRapide")

        try:
            client = Client(sid, token)
            client.messages.create(
                body=message_text,
                from_='whatsapp:+18575752654',  # Numéro WhatsApp Twilio
                to=f'whatsapp:{whatsapp_client}'
            )
            messages.success(request, "Message envoyé avec succès !")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'envoi : {str(e)}")

    return redirect("serviceRapide")
