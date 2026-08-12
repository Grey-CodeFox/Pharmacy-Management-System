from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('employee-registration', views.employee_reg,
         name="employee_registration"),
]
