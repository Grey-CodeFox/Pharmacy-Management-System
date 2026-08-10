from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Medicines)
admin.site.register(Unit)
