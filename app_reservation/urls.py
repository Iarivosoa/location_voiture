from .views import*
from django.urls import path
urlpatterns = [
    path('reservation/<int:id>',res, name='reservation'),
    path('reservation/', reservation, name='reserver'),
    # path('envoyer_whatsapp/', envoyer_whatsapp, name='envoyer_whatsapp'),
    path("serviceRapide",envoyer_whatsapp, name="envoyer_whatsapp"),
]
