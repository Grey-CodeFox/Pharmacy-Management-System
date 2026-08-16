from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class CustomUser(AbstractUser):
    role_choices = [
        ('staff', 'Staff'),
        ('cashier', 'Cashier')
    ]
    role = models.CharField(
        max_length=10, choices=role_choices, default="staff")
    username = models.CharField(unique=True)
    email = models.CharField(unique=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username
