from django.contrib import admin
from .models import Customer
# Register your models here.

class customerdisplay(admin.ModelAdmin):
    list_display=["customer","phone","city","state"]

admin.site.register(Customer, customerdisplay)