
from django.shortcuts import redirect, render
from itertools import product
from django.shortcuts import render
from methods import Details_context
from .models import *
from django.core.paginator import Paginator
from cart.models import *
from .forms import *
# Create your views here.

def all_reviews(request, id):
    review_list=Reviews.objects.filter(product_id=id).reverse()
    context={
        "review":review_list,
        "rat_list":rating_(id),
        'cart_item':len(Cart.objects.filter(customer_id=request.user.id)),
        'wishlist_item':len(Wishlist.objects.filter(customer_id=request.user.id))
    }
    context["product"]=Product.objects.get(id=id)
    return render(request, "review.html", context )


def rating_(id):
    if Reviews.objects.filter(product_id=id).count()==0:
        rat_list=[0,0,0,0,0]
        return rat_list
    else:
        total=Reviews.objects.filter(product_id=id).count()
        rat_list=[]
        a=0
        for i in range(1,6):
            rat=Reviews.objects.filter(product_id=id,rating=i).count()
            a+=rat*i
            value=rat*100/total
            value=round(value,2)
            rat_list.append(value)
        rat_list.append(str(a/total)[:3])

        return rat_list


def detail(request, item_id):
    cat=Product.objects.get(id=item_id).category_id
    context=Details_context(item_id)
    context["product"]=Product.objects.get(id=item_id)
    context["image"]=Other_image.objects.filter(product_id=item_id)
    context["list"]=Product.objects.filter(category=cat)
    context["ram_list"]=RAM.objects.filter(product_id=item_id)
    context["color"]=RAM.objects.filter(product_id=item_id)
    context['cart_item']=len(Cart.objects.filter(customer_id=request.user.id))
    context['wishlist_item']=len(Wishlist.objects.filter(customer_id=request.user.id))
    
    if request.method=="POST":
        massage=request.POST["massage"]
        rating=request.POST['RadioOptions']
        name=request.POST['name']
        email=request.POST['email']
        review=Reviews.objects.create(review=massage, rating=rating, name=name,email=email,product_id=item_id)
        review.save()
        add_rating_to_product(item_id)        
    return render(request, "detail.html", context)

def helpfull(request,review_id):
    review=Reviews.objects.get(id=review_id)
    review.helpfull+=1
    review.save()
    product_id=Reviews.object.get(id=review_id)
    redirect(f"/products/{product_id.product__id}")
        
def add_rating_to_product(id):
    rev=Reviews.objects.filter(product_id=id).count()
    a=0
    for i in range(1,6):
        rat=Reviews.objects.filter(product_id=id,rating=i).count()
        a+=rat*i
    rat=str(a/rev)[:3]

    item=Product.objects.get(id=id)
    item.review_count=rev
    item.rating_count=rat
    item.save()

def shop(request):
    product=Product.objects.all()
    context={
    "product":product,
    'cart_item':len(Cart.objects.filter(customer_id=request.user.id)),
    'wishlist_item':len(Wishlist.objects.filter(customer_id=request.user.id))
    }
    
    return render(request, "shop.html", context)


def category(request,itemCategory ):
    product_set=Product.objects.filter(category__id=itemCategory)
    context={
        "product":product_set,
        'cart_item':len(Cart.objects.filter(customer_id=request.user.id)),
        'wishlist_item':len(Wishlist.objects.filter(customer_id=request.user.id)),
        "path":f"Product: {Category_group.objects.get(sub_category=itemCategory).title}/ {Sub_category.objects.get(id=itemCategory).title}"
    }
    if request.GET:
        if request.GET['filter_by']:
            filter_type=request.GET['filter_by']
            if filter_type=="low_to_high":
                product_set=Product.objects.filter(category__id=itemCategory).order_by('price')
            elif filter_type=="high_to_low":
                product_set=Product.objects.filter(category__id=itemCategory).order_by('-price')
            elif filter_type=="rating":
                product_set=Product.objects.filter(category__id=itemCategory).order_by('-rating_count')
            else:
                product_set=Product.objects.filter(category__id=itemCategory)
            context["product"]=product_set
    return render(request, "shop.html",context)

def Group_category(request,category_sub):
    product_set=Product.objects.filter(category__group__id=category_sub)
    context={
        "product":product_set,
        'cart_item':len(Cart.objects.filter(customer_id=request.user.id)),
        'wishlist_item':len(Wishlist.objects.filter(customer_id=request.user.id)),
        "path":f"Product: {Category_group.objects.get(id=category_sub).title}/ "
    }
    return render(request, "shop.html",context)


    
