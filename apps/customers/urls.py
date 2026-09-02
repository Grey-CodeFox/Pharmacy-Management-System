
from django.urls import path
from . import views

urlpatterns = [
    path("", views.customer_home, name="customer_home"), path(
        "customer-add/", views.customer_add, name="customer_add"), path("customer-delete/<int:id>/", views.customer_delete, name="customer_delete"), path("customer-update/<int:id>", views.customer_update, name="customer_update"),
]
