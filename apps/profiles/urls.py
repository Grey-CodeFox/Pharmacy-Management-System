from django.urls import path
from . import views
urlpatterns = [
    path('', views.profile_login, name="profile_login"),
    path('employee-registration/', views.employee_reg,
         name="employee_registration"),
    path('logout/', views.profile_logout, name="profile_logout")
]
