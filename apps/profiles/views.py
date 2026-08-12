from django.shortcuts import render
from . import forms

# Create your views here.


def homepage(request):
    return render(request, 'profile_section/homepage.html')


def employee_reg(request):
    context = {'form': forms.Profiles}
    if request.user.is_superuser:
        return render(request, 'profile_section/employee_registration.html', context)
