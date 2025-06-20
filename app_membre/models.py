from django.db import models

# Create your models here.
class Insertion_membre(models.Model):

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    date_naissance = models.DateField()
    passsword = models.CharField(max_length=100)
    watsapp = models.IntegerField()
    pays = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
    class Meta:
        verbose_name = "Insertion Membre"
        verbose_name_plural = "Insertions Membres"