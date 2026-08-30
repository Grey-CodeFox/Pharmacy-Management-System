from django.shortcuts import render, redirect
from .models import Medicines
from . import forms
# Create your views here.


def medicine_home(request):
    medicine = Medicines.objects.all()
    return render(request, "medicines_section/medicines.html", {"medicine": medicine})


def medicine_add(request):
    form = forms.Medicine_Form()

    if request.method == "POST":
        form = forms.Medicine_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("medicine_home")
        else:
            return redirect("medicine_add", {"form": form})
    return render(request, "medicines_section/medicines-add.html", {"form": form})
