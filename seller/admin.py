from django.contrib import admin

from.models import Seller


class sellerstate(admin.ModelAdmin):

    list_display=["seller","company_name" ,"phone","city","state"]

admin.site.register(Seller,sellerstate)


