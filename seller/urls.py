from django.urls import path
from . import views

app_name='seller'

urlpatterns = [
    path('create/', views.seller, name="profile"  ),
    path('add_item/', views.add_item, name="add_item"  ),
    path('dashboard/', views.dashboard, name="dashboard"  ),
    path('delete/<int:item_id>', views.delete_product, name="delete_product"  ),
    path('', views.profile, name="profile"  ),
]