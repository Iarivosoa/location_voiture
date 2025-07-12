from django.contrib import admin
from .models import*
# Register your models here.

class Affiche_admin(admin.ModelAdmin):
    list_display =("nom_park","legende_park","description_park","detail","photo1","photo2","photo3","photo4","photo5","photo6")

admin.site.register(Site_park,Affiche_admin)