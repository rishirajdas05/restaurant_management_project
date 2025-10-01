from django.conf import settings
from django.shortcuts import render
from .models import MenuItem


def index(request):
    """
    Homepage: shows a welcome message and (optionally) fetches the menu via JS.
    Reads the restaurant name from settings (with a safe fallback).
    """
    context = {
        "restaurant_name": getattr(settings, "RESTAURANT_NAME", "My Restaurant"),
        # If you’re using the JS menu fetch on the homepage, keep/adjust this:
        "menu_api_url": "/orders/menu-api/",
    }
    return render(request, "index.html", context)


def menu_page(request):
    """
    Dedicated /menu/ page that renders MenuItem objects from the database.
    Includes a simple try/except so unexpected DB issues fail gracefully.
    """
    items = []
    error = None
    try:
        items = MenuItem.objects.order_by("name")
    except Exception as exc:  # pragma: no cover (basic safety)
        error = "Sorry, we couldn't load the menu right now. Please try again later."

    return render(request, "menu.html", {"items": items, "error": error})