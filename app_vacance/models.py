from django.db import models

# Create your models here.
class Site_park(models.Model):
    nom_park = models.CharField(max_length=250)
    legende_park = models.CharField(max_length=250)
    description_park = models.TextField()
    detail = models.CharField(max_length=250)
    photo1 = models.ImageField(upload_to="static/image/site_voyage")
    photo2 = models.ImageField(upload_to="static/image/site_voyage")
    photo3 = models.ImageField(upload_to="static/image/site_voyage")
    photo4 = models.ImageField(upload_to="static/image/site_voyage")
    photo5 = models.ImageField(upload_to="static/image/site_voyage")
    photo6 = models.ImageField(upload_to="static/image/site_voyage")

    # def __init__(self):
    #     return self.nom_park