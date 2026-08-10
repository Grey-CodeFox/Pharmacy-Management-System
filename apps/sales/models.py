from django.db import models
from apps.customers.models import Customers
from apps.medicines.models import Medicines
from django.conf import settings
# Create your models here.


class Sales(models.Model):
    customer = models.ForeignKey(
        Customers,
        on_delete=models.PROTECT,
        related_name="sales"
    )

    date = models.DateTimeField(
        auto_now_add=True
    )

    total = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    sold_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="sales"
    )

    def __str__(self):
        return f"Sale #{self.id}"


class SalesItems(models.Model):
    sale = models.ForeignKey(
        Sales, on_delete=models.CASCADE, related_name="items")

    medicine = models.ForeignKey(
        Medicines, on_delete=models.PROTECT, related_name="items"
    )

    qty = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.medicine.name}-{self.qty}"
