from django.db import models


from apps.categories.models import Category
from apps.suppliers.models import Supplier
# Create your models here.


class Unit(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Medicines(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='medicines/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    price = price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock_qty = models.PositiveIntegerField(
        default=0
    )
    reorder_level = models.PositiveIntegerField(
        default=10
    )
    expiry_date = models.DateField()
    batch_no = models.CharField(
        max_length=50
    )
    unit = models.ForeignKey(
        Unit,
        on_delete=models.PROTECT
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name
