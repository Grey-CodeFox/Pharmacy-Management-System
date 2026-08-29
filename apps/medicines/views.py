from django.shortcuts import render
from .models import Medicines
from . import forms
# Create your views here.


def medicine_home(request):
    form = forms.Medicine_Form
    return render(request, "medicines_section/medicines.html", {"form": form})
