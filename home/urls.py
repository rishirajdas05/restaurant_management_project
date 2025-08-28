from django.urls import path
from .views import *

urlpatterns = [ 
    path("", index, name="home"),
    path("about/",about,name="about"),
    path("contact/", views.contact, name="contact"),
    path("reservations/", views.reservations, name="reservations"),



]