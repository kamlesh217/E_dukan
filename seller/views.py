from multiprocessing import context
from django.shortcuts import render,redirect
from customer.models import *
from methods import Details_context
from products.forms import BOX_form, Battery_desc_form, Battery_power_form, Camera_desc_form, Camera_front_form, Camera_rear_form, Connectivity_technologies_form, Country_of_origin_form, Display_desc_form, Display_size_form, Item_weight_form, Manufacturer_form, OS_form, Other_image_form, RAM_form, ROM_form, SSD_form, Special_features_form
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
            return render(request, "seller_add_item.html",{"group":group})
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
            return render(request, "seller_add_item.html",context)
        else:
            return redirect("/seller/")
    else:
        return redirect("/customer/login")

def product_create(request,sub):
    if  request.user.is_authenticated:
        if Seller.objects.filter(seller=request.user.id):
            context={
            "product_create_path":f"Cateogry :{Sub_category.objects.get(id=sub).group}/{Sub_category.objects.get(id=sub).title}/",
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
                item.seller=Seller.objects.get(seller=request.user.id)
                item.save()
                return redirect(f"/seller/add_feature/{item.id}")

            return render(request, "seller_add_item.html",context)
        else:
            return redirect("/seller/")
    else:
        return redirect("/customer/login")

def add_feature(request,item_id):
    if  request.user.is_authenticated:
        if Seller.objects.filter(seller=request.user.id):
            sub=Product.objects.get(id=item_id).category.id
            context=Details_context(item_id)
            
            context["product_feature_path"]=f"Cateogry :{Sub_category.objects.get(id=sub).group}/{Sub_category.objects.get(id=sub).title}/\
                {Product.objects.get(id=item_id).product_name}"
            
            if request.method=="POST":
                name=request.POST["feature"]
                return redirect(f"/seller/add_item_feature/{name}/{item_id}")

            return render(request, "seller_add_item.html",context)
        else:
            return redirect("/seller/")
    else:
        return redirect("/customer/login")

def Create_item_feature(request,name,item_id):
    form=""
    if name=="SSD":
        if request.method == "POST":  
            form=SSD_form(request.POST)
    
    elif name=="ROM":
        if request.method == "POST": 
            form=ROM_form()
        else:

    
    elif name=="RAM":
        if request.method == "POST": 
            form=RAM_form()
        else:
            form=RAM_form()
    
    elif name=="OS":
        if request.method == "POST": 
            form=OS_form()
        else:
            form=OS_form()
    
    elif name=="Special_features":
        if request.method == "POST": 
            form=Special_features_form()
        else:
            form=Special_features_form()
    
    elif name=="Display_desc":
        if request.method == "POST": 
            form=Display_desc_form()
        else:
            form=Display_desc_form()

    
    elif name=="Display_size":
        if request.method == "POST": 
            form=Display_size_form()
        else:
            form=Display_size_form()
    
    elif name=="Battery_power":
        if request.method == "POST": 
            form=Battery_power_form()
        else:
    
    elif name=="Battery_desc":
        if request.method == "POST": 
            form=Battery_desc_form()
        else:
    
    elif name=="Camera_front":
        if request.method == "POST": 
            form=Camera_front_form()
        else:
    
    elif name=="Camera_rear":
        if request.method == "POST": 
            form=Camera_rear_form()
        else:
    
    elif name=="Camera_desc":
        if request.method == "POST": 
            form=Camera_desc_form()
        else:
    
    elif name=="Connectivity_technologies":
        if request.method == "POST": 
            form=Connectivity_technologies_form()
        else:
    
    elif name=="BOX":
        if request.method == "POST": 
            form=BOX_form()
        else:
    
    elif name=="Manufacturer":
        if request.method == "POST": 
            form=Manufacturer_form()
        else:
    
    elif name=="Country_of_origin":
        if request.method == "POST": 
         form=Country_of_origin_form()
        else:
    
    elif name=="Item_weight":
        if request.method == "POST": 
            form=Item_weight_form()
        else:
    
    elif name=="Other_image":
        if request.method == "POST": 
            form=Other_image_form()
        else:
    
    if form.is_valid:
        form.save()
        return redirect(f"/seller/add_item_feature/{name}/{item_id}")


    return render(request, "seller_form.html", {"forms":form})

