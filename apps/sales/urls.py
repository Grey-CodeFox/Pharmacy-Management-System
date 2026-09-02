
from django.urls import path
from . import views

urlpatterns = [
    path("", views.sale_home, name="sale_home"), path(
        "sale-add/", views.sale_add, name="sale_add"), path("sale-delete/<int:id>/", views.sale_delete, name="sale_delete")
]
