from .views import*
from django.urls import path

urlpatterns = [
    path('page_vacance',page_vacance,name="page_vacance"),
]
