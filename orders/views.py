from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
# from .serializers import MenuItemSerializer  # optional (see below)

class MenuAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # Hardcoded for now; replace with DB query later
        menu = [
            {"name": "Margherita Pizza", "description": "Classic tomato, mozzarella & basil.", "price": 250},
            {"name": "Veggie Burger", "description": "Grilled veg patty with fresh lettuce & sauces.", "price": 180},
            {"name": "Pasta Alfredo", "description": "Creamy Alfredo sauce with herbs.", "price": 220},
            {"name": "Cold Coffee", "description": "Chilled, frothy coffee with ice.", "price": 120},
        ]

        # If you want serializer validation/output formatting:
        # ser = MenuItemSerializer(menu, many=True)
        # return Response(ser.data)

        return Response(menu)