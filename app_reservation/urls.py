from .views import*
from django.urls import path
urlpatterns = [
    path('reservation/<int:id>', reservation, name='reservation'),
]
