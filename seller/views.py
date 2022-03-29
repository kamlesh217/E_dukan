from multiprocessing import context
from django.shortcuts import render,redirect
from customer.models import *
from seller.models import *
from products.models import *

# Create your views here.
def seller(request):
    if  request.user.is_authenticated:
        if Seller.objects.filter(seller=request.user):
            return redirect("/seller/dashboard")

        if request.method=="POST":
            company_name=request.POST["name"]
            email=request.POST["email"]
            phone=request.POST["phone"]
            address=request.POST["address"]
            city=request.POST["city"]
            state=request.POST["state"]
            zipcode=request.POST["zip"]
 
            seller_user=Seller(company_phone=phone,address=address,city=city,state=state,zip=zipcode,
            seller=request.user,company_name=company_name,company_email=email)
            seller_user.save()
            return redirect("/")
    
    return render(request, "seller.html")

def dashboard(request):
    seller_account=Seller.objects.get(seller=request.user.id)
    item_list=Product.objects.filter(seller=seller_account)
    context={
        "item_list":item_list
    }
    return render(request, "seller_dashboard.html",context)

def profile(request):
    return render(request, "seller_dashboard.html")

def delete_product(request,item_id):

    item=Product.objects.filter(id=item_id)
    item.delete()
    return redirect("/seller/dashboard")

