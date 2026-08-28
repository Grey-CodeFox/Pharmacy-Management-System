from django.shortcuts import render, redirect
from .models import Supplier
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
        supplier.name = request.POST.get("name")
        supplier.contact_person = request.POST.get("contact_person")
        supplier.phone = request.POST.get("phone")
        supplier.email = request.POST.get("email")
        supplier.address = request.POST.get("address")

        supplier.save()
        return redirect("supplier_home")

    return render(request, "suppliers_section/supplier-update.html", {"supplier": supplier})


def supplier_delete(request):
    pass
