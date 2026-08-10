from django.db import models

# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=200, unique=True)
    contact_person = models.CharField(
        max_length=100
    )
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name
