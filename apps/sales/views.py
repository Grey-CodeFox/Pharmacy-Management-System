from django.shortcuts import render, redirect
from .forms import Sales_Form, Sales_Item_Form, Sales_Item_FormSet
from .models import *
from apps.medicines.models import Medicines
from django.contrib import messages
# Create your views here.


def sale_home(request):
    sales = Sales.objects.all()

    return render(
        request,
        "sales_section/sales.html",
        {
            "sales": sales
        }
    )


def sale_add(request):

    medicines = Medicines.objects.all()

    if request.method == "POST":

        sale_form = Sales_Form(request.POST)

        item_formset = Sales_Item_FormSet(request.POST)

        if sale_form.is_valid() and item_formset.is_valid():

            items = item_formset.save(commit=False)
            # Check stock first
            for item in items:
                if item.qty > item.medicine.stock_qty:
                    messages.error(
                        request,
                        f"Not enough stock for {item.medicine.name}. "
                        f"Available: {item.medicine.stock_qty}"
                    )

                    return render(
                        request,
                        "sales_section/sales-add.html",
                        {
                            "saleForm": sale_form,
                            "item_formset": item_formset,
                            "medicines": medicines,
                        }
                    )
            # Create sale
            sale = sale_form.save(commit=False)

            sale.sold_by = request.user

            sale.total = 0

            sale.save()

            total = 0

            for item in items:

                item.sale = sale

                item.price = item.medicine.price

                item.subtotal = (
                    item.qty * item.price
                )

                item.save()
                # Reduce stock
                item.medicine.stock_qty -= item.qty
                item.medicine.save()
                total += item.subtotal

            sale.total = total

            sale.save()

            return redirect("sale_home")

    else:

        sale_form = Sales_Form()

        item_formset = Sales_Item_FormSet()

    return render(
        request,
        "sales_section/sales-add.html",
        {
            "saleForm": sale_form,
            "item_formset": item_formset,
            "medicines": medicines,
        }
    )


def sale_delete(request, id):

    sale = Sales.objects.get(id=id)

    if request.method == "POST":
        sale.delete()
        return redirect("sale_home")

    return render(
        request,
        "sales_section/sales-delete.html",
        {
            "sale": sale
        }
    )
