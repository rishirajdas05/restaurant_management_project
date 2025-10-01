from django.urls import path
from .views import *

urlpatterns = [ 
    path("", index, name="home"),
    path("about/",about,name="about"),
    path("contact/", views.contact, name="contact"),
    path("reservatiopath("feedback/", views.feedback, name="feedback"),
    path("feedback/", views.feedback, name="feedback"),
    path("", views.index, name="home"),
    path("menu/", views.menu_page, name="menu_page"),



]