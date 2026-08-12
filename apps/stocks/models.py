from django.db import models
from apps.medicines.models import Medicines
from django.conf import settings
# Create your models here.


class StockLogs(models.Model):

    type_choices = [
        ('in', 'Stock In'), ('out', 'Stock Out'), ('sale', 'Sale')
    ]

    medicine_id = models.ForeignKey(
        Medicines, on_delete=models.CASCADE, related_name="stockLog")
    type = models.CharField(choices=type_choices, max_length=10)
    qty = models.PositiveIntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True)
    logged_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
