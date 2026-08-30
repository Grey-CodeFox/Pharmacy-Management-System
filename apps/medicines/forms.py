from .models import Medicines
from django import forms
from django.utils import timezone


class Medicine_Form(forms.ModelForm):
    class Meta:
        model = Medicines
        fields = ["name", "image", "category", "supplier",
                  "price", "stock_qty", "reorder_level", "expiry_date", "batch_no", "unit"]

        widgets = {
            "expiry_date": forms.DateInput(
                attrs={"type": "date", "min": timezone.localdate().isoformat()},

            )
        }

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price <= 0:
            raise forms.ValidationError("Price Should Not Be less than 0 or 0")
        return price

    def clean_stock_qty(self):
        stock = self.cleaned_data["stock_qty"]
        if stock <= 0:
            raise forms.ValidationError(
                "Stock Should Not Be less than 0 or 0")
        return stock

    def clean_expiry_date(self):
        expiry = self.cleaned_data["expiry_date"]
        today = timezone.localdate()
        if expiry <= today:
            raise forms.ValidationError(
                "Expiry date must be after today."
            )
        return expiry
