from django import forms
from .models import CustomUser


class Profiles(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role']
