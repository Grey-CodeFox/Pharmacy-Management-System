from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Profiles
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm
)

# Create your views here.


def login(request):
    if request.method == "POST":
        forms = AuthenticationForm(data=request.POST)
        if forms.is_valid():
            user = forms.get_user()
            login(request, user)
            return redirect("dashboard")
        else:
            return redirect("login")

    else:
        forms = AuthenticationForm()
    return render(request, 'profile_section/login.html', {"forms": forms})


@login_required
def logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")


@login_required
def employee_reg(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Access denied")
    if request.method == "POST":
        forms = Profiles(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("login")
    else:
        forms = Profiles()
    return render(request, 'profile_section/employee_registration.html', {"forms": forms})
