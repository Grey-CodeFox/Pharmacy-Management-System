from .models import Sales, SalesItems
from django import forms
from django.forms import inlineformset_factory


class Sales_Form(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ["customer"]


class Sales_Item_Form(forms.ModelForm):
    class Meta:
        model = SalesItems
        fields = ["medicine", "qty"]


Sales_Item_FormSet = inlineformset_factory(
    Sales,
    SalesItems,
    form=Sales_Item_Form,
    extra=0
)
