from django.urls import path
from . import views

app_name='customer'

urlpatterns = [
    path('register/', views.register, name="register"  ),
    path('login/', views.signin, name="login" ),
    path('logout/', views.signout, name="logout" ),
    path('orders/', views.orders, name="orders"  ),
    path('profile/', views.profile, name="profile"  ),
]