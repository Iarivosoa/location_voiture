from django.db import models
from django.utils import timezone
# Create your models here.
class Insertion_voiture(models.Model):
    nom = models.CharField(max_length=150)
    description = models.TextField()
    types = models.CharField(max_length=150)
    marque = models.CharField(max_length=150)
    disponibilite = models.BooleanField(default=True)
    prix = models.FloatField()
    photo = models.ImageField(upload_to="static/image")
    photo2 = models.ImageField(upload_to="static/image")
    photo3 = models.ImageField(upload_to="static/image")
    photo4 = models.ImageField(upload_to="static/image")
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nom
