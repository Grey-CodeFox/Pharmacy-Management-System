from django.urls import path
from . import views

urlpatterns = [
    path("", views.supplier_home, name="supplier_home"),
    path("supplier-add/", views.supplier_add, name="supplier_add"),
    path("supplier-update/<int:id>", views.supplier_update, name="supplier_update"),
    path("supplier-delete/<int:id>", views.supplier_delete, name="supplier_delete"),

]
