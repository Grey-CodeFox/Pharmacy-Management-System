from django.urls import path
from . import views
urlpatterns = [
    path('', views.login, name="login"),
    path('employee-registration/', views.employee_reg,
         name="employee_registration"),
]
