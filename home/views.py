# home/views.py
from django.conf import settings
from django.shortcuts import render
from urllib.parse import quote_plus

def index(request):
    name = getattr(settings, "RESTAURANT_NAME", "My Restaurant")
    addr = getattr(settings, "RESTAURANT_ADDRESS", "123, Main Street, Gwalior, MP 474001, India")

    context = {
        # If you already show the menu via JS fetch, keep your API URL here:
        "menu_api_url": "/orders/menu-api/",
        "restaurant_name": name,
        "restaurant_address": addr,
        # Simple iframe embed using the address
        "maps_embed_src": f"https://www.google.com/maps?q={quote_plus(addr)}&output=embed",
    }
    return render(request, "index.html", context)