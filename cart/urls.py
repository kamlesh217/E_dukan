from django.urls import path
from . import views

app_name='cart'

urlpatterns = [
    path('<int:item_id>/', views.Add_to_cart , name="Add_to_cart"  ),   
    path('add/<int:item_id>/', views.add_one_cart , name="add_one_cart"  ),
    path('remove/<int:item_id>/', views.remove_one_cart , name="remove_one_cart"  ),
    path('delete/<int:item_id>/', views.delect_from_cart , name="delect_from_cart"  ),
    path('cart_to_wishlist/<int:item_id>/', views.cart_to_wishlist , name="cart_to_wishlist"  ),
    path('wish_to_cart/<int:item_id>/', views.wish_to_cart , name="wish_to_cart" ),
    path('delete_wish/<int:item_id>/', views.delect_from_wishlist , name="delect_from_wishlist"  ),
    path('add_wish/<int:item_id>/', views.add_to_wishlist, name="add_to_wishlist"  ),
    path('', views.cart , name="cart"  ),
    path('wishlist/', views.wishlist , name="wishlist"),
]

                                         
