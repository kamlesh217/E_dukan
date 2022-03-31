from django.urls import path
from . import views

app_name='seller'

urlpatterns = [
    path('create/', views.seller, name="seller"  ),
    path('category/', views.category_group, name="category_group"  ),
    path('sub_category/<int:category>/', views.category_sub, name="category_sub"  ),
    path('add_item/<int:sub>/', views.product_create, name="product_create"  ),
    path('dashboard/', views.dashboard, name="dashboard"  ),
    path('delete/<int:item_id>', views.delete_product, name="delete_product"  ),
    path('', views.profile, name="profile"  ),

]