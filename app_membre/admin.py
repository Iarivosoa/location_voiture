from django.contrib import admin
from .models import Insertion_membre
# Register your models here.

class Affiche_membre(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email','passsword','watsapp','pays')
admin.site.register(Insertion_membre, Affiche_membre)
