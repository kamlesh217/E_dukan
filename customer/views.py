from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, "register.html")

def signin(request):
    return render(request, "login.html")

def signout(request):
    return render(request, "login.html")

def orders(request):
    return render(request, "orders.html")

def profile(request):
    return render(request, "profile.html")

