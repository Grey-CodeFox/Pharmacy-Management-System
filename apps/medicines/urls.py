from django.urls import path
from . import views

urlpatterns = [
    path("", views.medicine_home, name="medicine_home"),
    path("medicine-add/", views.medicine_add, name="medicine_add"),
    path("medicine-update/<int:id>/",
         views.medicine_update, name="medicine_update"),
    path("medicine-delete/<int:id>/",
         views.medicine_delete, name="medicine_delete")
]
