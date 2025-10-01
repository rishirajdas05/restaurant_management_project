from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class MenuItem(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)  # optional
    price = models.DecimalField(
        max_digits=8, decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name