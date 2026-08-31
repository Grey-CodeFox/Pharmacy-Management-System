from django.shortcuts import render, redirect
from .models import Customers
from . import forms

# Create your views here.


def customer_home(request):
    return render(request, "customers_section/customers.html")


def customer_add(request):
    form = forms.Customers_Form()
    if request.method == "POST":
        form = forms.Customers_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("customer_home")
        else:
            return render(request, "customers_section/customers-add.html", {"form": form})
    return render(request, "customers_section/customers-add.html", {"form": form})


def customer_update(request, id):
    customer = Customers.objects.get(id=id)
    if request.method == "POST":
        form = forms.Customers_Form(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_home')

    else:
        form = forms.Customers_Form(instance=customer)
    return render(request, "customers_section/customers-update.html", {"form": form})


def customer_delete(request):
    customer = Customers.objects.get(id=id)

    if request.method == "POST":
        customer.delete()
        return redirect("customer_home")
    return redirect("customer_home")
