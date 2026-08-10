from django.db import models

# Create your models here.


class Customers(models.Model):
    name = models.CharField(
        max_length=150
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    purchases = models.PositiveIntegerField()

    def __str__(self):
        return self.name
