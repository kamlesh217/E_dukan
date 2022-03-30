from multiprocessing import context
from django.shortcuts import render,redirect
from customer.models import *
from seller.models import *
from products.models import *

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
            return redirect("/seller/dashboard")
        return render(request, "seller_register.html")
    else:    
        return redirect("/customer/login")

def dashboard(request):
    if  request.user.is_authenticated:
        if Seller.objects.filter(seller=request.user.id):
            seller_account=Seller.objects.get(seller=request.user.id)
            item_list=Product.objects.filter(seller=seller_account)
            context={
            "item_list":item_list
            }
            return render(request, "seller_dashboard.html",context)
        else:
            return redirect("/seller")
    else:
        return redirect("/customer/login")

def profile(request):
    if  request.user.is_authenticated:
        if Seller.objects.filter(seller=request.user.id):
            d=0
        else:
            return redirect("/seller/")
    else:
        return redirect("/customer/login")
        

    return render(request, "seller_dashboard.html")

def delete_product(request,item_id):
    if  request.user.is_authenticated:
        if Seller.objects.filter(seller=request.user.id):
            item=Product.objects.filter(id=item_id)
            item.delete()
            return redirect("/seller/dashboard")
        else:
            return redirect("/seller/")
    else:
        return redirect("/customer/login")
        

def category_group(request):
    if  request.user.is_authenticated:
        if Seller.objects.filter(seller=request.user.id):
            group=Category_group.objects.all()
            if request.method=="POST":
                category=request.POST["category"]
                return redirect(f"/seller/sub_category/{category}")
            return render(request, "add_item.html",{"group":group})
        else:
            return redirect("/seller/")
    else:
        return redirect("/customer/login")
        

def category_sub(request,category):
    if  request.user.is_authenticated:
        if Seller.objects.filter(seller=request.user.id):

            sub_group=Sub_category.objects.filter(group_id=category)
            if request.method=="POST":
                sub=request.POST["sub_category"]
                return redirect(f"/seller/add_item/{sub}")
            context={
                "sub_group":sub_group,
                "path":f"Cateogry :{Category_group.objects.get(id=category).title}/"
            }
            return render(request, "add_item.html",context)
        else:
            return redirect("/seller/")
    else:
        return redirect("/customer/login")

def product_create(request,sub):
    if  request.user.is_authenticated:
        if Seller.objects.filter(seller=request.user.id):
            context={
            "product_path":f"Cateogry :{Sub_category.objects.get(id=sub).group}/{Sub_category.objects.get(id=sub).title}/",
            }
            if request.method=="POST":
                name=request.POST["name"]
                price=request.POST["price"]
                discount=request.POST["discount"]
                a_price=request.POST["a_price"]
                brand=request.POST["brand"]
                m_name=request.POST["m_name"]
                qty=request.POST["qty"]
                desc=request.POST["desc"]
                image=request.POST["image"]

                item=Product(category_id=sub,image=image,product_name=name,price=price,discount=discount,
                qty=qty,desc=desc,actual_price=a_price,brand=brand,model_name=m_name)
                item.seller_id=request.user.id
                item.save()

            return render(request, "add_item.html",context)
        else:
            return redirect("/seller/")
    else:
        return redirect("/customer/login")