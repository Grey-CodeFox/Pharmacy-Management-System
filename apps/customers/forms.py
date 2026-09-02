from .models import Customers
from django import forms


class Customers_Form(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ["name", "phone", "email", "address"]
        widgets = {
            "phone": forms.TextInput(
                attrs={
                    "minlength": "10",
                    "maxlength": "20"
                }
            ),
        }

    def clean_phone(self):
        phone = self.cleaned_data["phone"]

        if not phone.isdigit():
            raise forms.ValidationError(
                "Phone number must contain only digits."
            )

        if len(phone) != 10:
            raise forms.ValidationError(
                "Phone number must be exactly 10 digits."
            )

        return phone
