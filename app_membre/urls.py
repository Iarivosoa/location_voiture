from django.urls import path
from.views import*

urlpatterns = [
    path("page_connexion",page_connexion,name="page_connexion"),
    path("page_souscription",page_souscription,name="page_souscription")
]
