from django.contrib import admin
from .models import Insertion_voiture
# Register your models here.
class affiche_voiture(admin.ModelAdmin):
    list_display = ("nom","description","types","marque","disponibilite","prix","photo","photo2","photo3","photo4","date")
admin.site.register(Insertion_voiture,affiche_voiture)
