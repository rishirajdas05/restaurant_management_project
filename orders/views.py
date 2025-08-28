from django.shortcuts import render

def menu_list(request):
    # Hardcoded menu list for now
    menu_items = [
        {"id": 1, "name": "Margherita Pizza", "price": 250},
        {"id": 2, "name": "Veggie Burger", "price": 180},
        {"id": 3, "name": "Pasta Alfredo", "price": 220},
        {"id": 4, "name": "Cold Coffee", "price": 120},
    ]
    return render(request, "menu_list.html", {"menu_items": menu_items})    
    
    
except Exception as e:
    # Log error for debugging (in real apps use logging)
    print(f"Error in menu_list view: {e}")
    return HttpResponseServerError(
        "<h1>Something went wrong 😢</h1><p>Please try again later.</p>"
        )