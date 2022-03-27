from django.urls import path
from . import views

app_name='core'

urlpatterns = [
    path("", views.index, name="index"),
    path('cart/', views.cart , name="cart"  ),
    path('checkout/', views.checkout, name="checkout"  ),
    path('contact/', views.contact,name="contact"),
    
]