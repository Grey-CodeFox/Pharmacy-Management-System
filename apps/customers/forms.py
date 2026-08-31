from .models import Customers
from django import forms


class Customers_Form(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ["name", "phone", "email", "address"]
