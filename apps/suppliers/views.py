from django.shortcuts import render, redirect
from .models import Supplier
from django.contrib import messages
# Create your views here.


def supplier_home(request):
    supplier = Supplier.objects.all()
    return render(request, "suppliers_section/supplier.html", {"supplier": supplier})


def supplier_add(request):
    if request.method == "POST":
        get_name = request.POST.get("name")
        get_contact = request.POST.get("contact_person")
        get_phone = request.POST.get("phone")
        get_email = request.POST.get("email")
        get_address = request.POST.get("address")

        if (Supplier.objects.filter(name=get_name).exists()):
            messages.error(request, "supplier name already exist")
            return redirect("supplier_add")
        elif (Supplier.objects.filter(email=get_email).exists()):
            messages.error(request, "email already exist")
            return redirect("supplier_add")

        if (get_phone.isdigit() == False or len(get_phone) != 10):
            messages.error(request, "Phone number must be exactly 10 digits.")
            return redirect("supplier_add")

        supplier = Supplier(
            name=get_name,
            contact_person=get_contact,
            phone=get_phone,
            email=get_email,
            address=get_address,
        )

        supplier.save()
        return redirect("supplier_home")
    return render(request, "suppliers_section/supplier-add.html")


def supplier_update(request, id):
    supplier = Supplier.objects.get(id=id)

    if request.method == "POST":
        get_name = request.POST.get("name")
        get_contact = request.POST.get("contact_person")
        get_phone = request.POST.get("phone")
        get_email = request.POST.get("email")
        get_address = request.POST.get("address")

        if (Supplier.objects.filter(name=get_name).exclude(id=id).exists()):
            messages.error(request, "supplier name already exist")
            return redirect("supplier_update", id=id)
        elif (Supplier.objects.filter(email=get_email).exclude(id=id).exists()):
            messages.error(request, "email already exist")
            return redirect("supplier_update", id=id)

        if (get_phone.isdigit() == False or len(get_phone) != 10):
            messages.error(request, "Phone number must be exactly 10 digits.")
            return redirect("supplier_update", id=id)
        supplier.name = get_name
        supplier.contact_person = get_contact
        supplier.phone = get_phone
        supplier.email = get_email
        supplier.address = get_address

        supplier.save()
        return redirect("supplier_home")

    return render(request, "suppliers_section/supplier-update.html", {"supplier": supplier})


def supplier_delete(request, id):
    supplier = Supplier.objects.get(id=id)

    if request.method == "POST":
        supplier.delete()
        return redirect("supplier_home")
    return redirect("supplier_home")
