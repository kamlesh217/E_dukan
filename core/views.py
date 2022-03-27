from django.shortcuts import render

from products.models import Product


# Create your views here.

def index(request):
    latest=Product.objects.all().reverse()[:8]

    return render(request, "index.html",{'latest':latest})

def cart(request):
    return render(request, "cart.html")

def checkout(request):
    return render(request, "checkout.html")

def contact(request):
    return render(request, "contact.html")

