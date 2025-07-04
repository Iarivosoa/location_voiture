from django.shortcuts import render, redirect
from .models import Reservation
from app_membre.models import Insertion_membre
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
import random, string
from django.conf import settings

# Create your views here.
def reservation(request, id=None):
    if request.method == "POST":
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        telephone = request.POST.get('telephone')
        ville_depart = request.POST.get('ville_depart')
        compagnie_vol = request.POST.get('compagnie_vol')
        date_depart = request.POST.get('date_depart')
        nombre_personnes = request.POST.get('nombre_personnes')
        bagages = request.POST.get('bagages') == 'True'
        commentaire = request.POST.get('commentaire')

        # Création ou récupération du client (Insertion_membre)
        client, created = Insertion_membre.objects.get_or_create(
            nom=nom, prenom=prenom, defaults={
                'email': '', 'date_naissance': timezone.now(), 'passsword': '', 'watsapp': 0, 'pays': ''
            }
        )
        # Générer un numéro de réservation unique
        numero_reservation = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        while Reservation.objects.filter(numero_reservation=numero_reservation).exists():
            numero_reservation = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

        reservation_obj = Reservation.objects.create(
            client=client,
            ville_depart=ville_depart,
            compagnie_vol=compagnie_vol,
            date_depart=date_depart,
            nombre_personnes=nombre_personnes,
            bagages=bagages,
            commentaire=commentaire,
            numero_reservation=numero_reservation
        )
        # Envoi d'un email de confirmation si l'email du client existe
        
        if client.email:
            send_mail(
                'Confirmation de votre réservation de taxi auprès de TAXI EXPRESS avec le Teams Express',
                f'Bonjour {client.prenom},\n\nVotre réservation a bien été enregistrée.\nNuméro de réservation : {numero_reservation}\nDépart : {ville_depart}\nCompagnie de vol : {compagnie_vol}\nDate et heure : {date_depart}\n\nMerci d\'avoir choisi notre service !',
                settings.EMAIL_HOST_USER ,
                [client.email],
                fail_silently=True,
            )
        messages.success(request, f"Votre réservation a bien été enregistrée ! Numéro : {numero_reservation}")
        return redirect('reservation', id=reservation_obj.id)

    return render(request, 'reservation.html')