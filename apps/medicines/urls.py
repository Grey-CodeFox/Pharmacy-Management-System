from django.urls import path
from . import views

urlpatterns = [
    path("", views.medicine_home, name="medicine_home"),
    path("medicine-add/", views.medicine_add, name="medicine_add")
]
