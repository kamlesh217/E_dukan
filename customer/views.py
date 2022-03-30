
from django.shortcuts import redirect, render
from cart.models import *
from django.contrib import messages
from core.models import  OrderItems
from .models import *
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":
            fname=request.POST["fname"]
            lname=request.POST["lname"]
            phone=request.POST["phone"]
            address=request.POST["address"]
            city=request.POST["city"]
            state=request.POST["state"]
            zipcode=request.POST["zip"]
            username=request.POST["email"]
            password=request.POST["password"]

            if Customer.objects.filter(customer__username=username):
                messages.success(request, 'Email already Exists')
                return redirect('/customer/register')
            else:
                user=User.objects.create_user(username=username,
                email=username,
                first_name=fname,
                last_name=lname,
                password=password)
                user.save()   
                customer_user=Customer(phone=phone,address=address,city=city,state=state,zip=zipcode,
                customer=user)
                customer_user.save()
                log=authenticate(username=username, password=password)
                if user is not None:
                    login(request, log)
                    return redirect("/")
        return render(request, "register.html")
    

def signin(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":
            username=request.POST["email"]   
            password=request.POST["password"]

            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.success(request, 'Enter valid details')
                return redirect('/customer/login')
        context={'cart_item':len(Cart.objects.filter(customer_id=request.user.id)),
        'wishlist_item':len(Wishlist.objects.filter(customer_id=request.user.id))}

        return render(request, "login.html",context)
    
    

def signout(request):
    if  request.user.is_authenticated:
        logout(request)
    return redirect("/")

def orders(request):
    
    if  request.user.is_authenticated:
        context=[]
        order_list=OrderItems.objects.filter(order__customer=request.user.pk)
        context={
            "order_list":order_list,
            'cart_item':len(Cart.objects.filter(customer_id=request.user.id)),
            'wishlist_item':len(Wishlist.objects.filter(customer_id=request.user.id))
            }

        return render(request, "orders.html",context)
    else:   
        return redirect("/customer/login")

def profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html")
    else:
        return redirect("/customer/login")

