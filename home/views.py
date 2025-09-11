from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! We’ve received your contact info.")
            return redirect("home")
    else:
        form = ContactForm()

    return render(request, "index.html", {
        "form": form,
        "menu_api_url": "/orders/menu-api/"  # keep your menu API from earlier
    })