from decimal import Decimal
from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=15)

    @property
    def sale_price(self):
        return f"{Decimal(self.price):.2f}"
