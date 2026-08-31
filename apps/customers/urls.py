from django.urls import path
from . import views


from django.urls import path
from . import views

urlpatterns = [
    path("", views.customer_home, name="customer_home"), path(
        "customer-add/", views.customer_add, name="customer_add"), path("customer-delete/<int:id>/", views.customer_delete, name="customer_delete"), path("customer-update/<int:id>", views.customer_update, name="customer_update"),
]


# urlpatterns = [
#     path("", views.medicine_home, name="medicine_home"),
#     path("medicine-add/", views.medicine_add, name="medicine_add"),
#     path("medicine-update/<int:id>/",
#          views.medicine_update, name="medicine_update"),
#     path("medicine-delete/<int:id>/",
#          views.medicine_delete, name="medicine_delete")
# ]
