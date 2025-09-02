from django.urls import path
from .views import *

urlpatterns = [
    path("menu-api/", MenuAPIView.as_view(), name="menu_api"),
]