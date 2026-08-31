from django.shortcuts import render, redirect
from .models import Medicines
from . import forms
from datetime import datetime, timedelta, date
# Create your views here.


def medicine_home(request):
    medicine = Medicines.objects.all()
    today = date.today()
    expiry_warning_date = today + timedelta(days=30)
    return render(request, "medicines_section/medicines.html", {"medicine": medicine, "today": today, "expiry_alert": expiry_warning_date})


def medicine_add(request):
    form = forms.Medicine_Form()

    if request.method == "POST":
        form = forms.Medicine_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("medicine_home")
        else:
            return render(request, "medicines_section/medicines-add.html", {"form": form})
    return render(request, "medicines_section/medicines-add.html", {"form": form})


def medicine_update(request, id):
    medicine = Medicines.objects.get(id=id)
    if request.method == "POST":
        form = forms.Medicine_Form(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medicine_home')

    else:
        form = forms.Medicine_Form(instance=medicine)
    return render(request, "medicines_section/medicines-update.html", {"form": form})


def medicine_delete(request, id):
    medicine = Medicines.objects.get(id=id)

    if request.method == "POST":
        medicine.delete()
        return redirect("medicine_home")
    return redirect("medicine_home")
