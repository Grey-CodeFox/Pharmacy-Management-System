
from django.urls import path
from . import views

urlpatterns = [
    path("", views.category_home, name="category_home"),
    path("category-add/", views.category_add, name="category_add"),
    path("category-update/<int:id>/",
         views.category_update, name="category_update"),
    path(
        "category-delete/<int:id>/",
        views.category_delete,
        name="category_delete"
    )
]
