from itertools import product
from multiprocessing import context
from django.shortcuts import redirect, render

from cart.models import *
from .models import *
from products.models import Product


# Create your views here.

def index(request):
    context={
        'cart_item':len(Cart.objects.filter(customer_id=request.user.id)),
        'wishlist_item':len(Wishlist.objects.filter(customer_id=request.user.id)),
        'latest':Product.objects.all().reverse()[:8]
        }
    return render(request, "index.html",context)


def checkout(request):
    if request.user.is_authenticated:
        item_list=Cart.objects.filter(customer_id=request.user.id)
        subtotal=float()
        for i in range(len(item_list)):
            subtotal+=item_list[i].product.price*item_list[i].qty

        context={'item':item_list,
        'subtotal':subtotal,
        'total':subtotal+100,
        'cart_item':len(Cart.objects.filter(customer_id=request.user.id)),
        'wishlist_item':len(Wishlist.objects.filter(customer_id=request.user.id))
        }

        if request.method=="POST":
            name=request.POST["name"]
            phone=request.POST["phone"]
            address=request.POST["address"]
            city=request.POST["city"]
            zip=request.POST["pincode"]
            state=request.POST["state"]
            email=request.POST["email"]

            if OrderDetails.objects.all():
                orderNo=OrderDetails.objects.all().reverse()[0].orderNo+1
            else:
                orderNo=1
            a=orderNo

            order_details=OrderDetails(name=name,customer=request.user.id,phone=phone,
            address=address,city=city,zipcode=zip,state=state,email=email,
            orderNo=a,total=subtotal+100)
            order_details.save()

            for item in range(len(item_list)):
                items=OrderItems(qty=item_list[i].qty, totalPrice=item_list[i].product.price*item_list[i].qty,
                productID=item_list[0].product,order= order_details)
                items.save()
            
            item_list.delete()
            return redirect("/customer/orders/")        
        return render(request, "checkout.html", context)

    return redirect("/customer/login")

def contact(request):
    context={
        'cart_item':len(Cart.objects.filter(customer_id=request.user.id)),
        'wishlist_item':len(Wishlist.objects.filter(customer_id=request.user.id))
        }
    return render(request, "contact.html",context)

