
from stringprep import c22_specials
from django.shortcuts import render
from methods import Details_context
from .models import *
# Create your views here.

def all_reviews(request, id):
    review_list=Reviews.objects.filter(product_id=id).reverse()
    context={
        "review":review_list,
        "rat_list":rating_(id)
    }
    context["product"]=Product.objects.get(id=id)
    return render(request, "review.html", context )


def rating_(id):
    if Reviews.objects.filter(product_id=id).count==0:
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


    if request.method=="POST":
        massage=request.POST["massage"]
        rating=request.POST['RadioOptions']
        name=request.POST['name']
        email=request.POST['email']
        print(massage,rating,name,email)
        review=Reviews.objects.create(review=massage, rating=rating, name=name,email=email,product_id=item_id)
        review.save()
        
    
    return render(request, "detail.html", context)

def category(request,itemCategory ):
    product_cat=Sub_category.objects.filter(group__title=itemCategory)
    product_set=Product.objects.filter(category=product_cat[0])
    for i in range(len(product_cat)):
        a=Product.objects.filter(category=product_cat[i])
        product_set= product_set | a
    
    return render(request, "shop.html",{"product":product_set})

def shop(request):
    context={
    "product":Product.objects.all(),
    }
    return render(request, "shop.html", context)



