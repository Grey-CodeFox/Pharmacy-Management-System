from django.shortcuts import render, redirect
from .models import Category
# Create your views here.


def category_home(request):
    category = Category.objects.all()
    return render(request, "categories_section/categories.html", {"category": category})


def category_add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = Category(name=name, description=description)
        category.save()
        return redirect("category_home")
    return render(request, "categories_section/category-add.html")


def category_update(request, id):
    category = Category.objects.get(id=id)
    if request.method == "POST":
        category.name = request.POST.get('name')
        category.description = request.POST.get('description')
        category.save()
        return redirect("category_home")
    context = {
        "get_name": category.name,
        "get_description": category.description,
        "get_id": category.id,
    }
    return render(request, "categories_section/category-update.html", context)


def category_delete(request, id):
    category = Category.objects.get(id=id)
    if request.method == "POST":
        category.delete()
        return redirect("category_home")
    return redirect("category_home")
