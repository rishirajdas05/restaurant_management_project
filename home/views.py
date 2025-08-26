from django.shortcuts import render
from django.conf import settings

def index(request):
    return render(request, "home/index.html")
def about(request):
    return render(request, "about.html")
def index(request):
    context = {
        "restaurant_name": settings.RESTAURANT_NAME
    }
    return render(request, "index.html", context)
def index(request):
    context = {
        "restaurant_phone": settings.RESTAURANT_PHONE
    }
    return render(request, "index.html", context)
    
def index(request):
    context = {
        "restaurant_name": "Foodie Paradise",
        "restaurant_phone": getattr(settings, "RESTAURANT_PHONE", "+91 98765 43210")
    }
    return render(request, "index.html", context)  
    # Create your views here.