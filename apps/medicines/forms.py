from .models import Medicines
from django import forms


class Medicine_Form(forms.ModelForm):
    class Meta:
        model = Medicines
        fields = ["name", "image", "category", "supplier",
                  "price", "stock_qty", "reorder_level", "expiry_date", "batch_no", "unit"]

        widgets = {
            "expiry_date": forms.DateInput(
                attrs={"type": "date"}
            )
        }
