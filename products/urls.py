from django.urls import path
from products import views

app_name='products'

urlpatterns = [
    path('<int:item_id>/', views.detail , name="item_detail" ),
    path('<int:id>/reviews', views.all_reviews , name="all_reviews" ),
    path('shop/', views.shop, name="shop" ),
    path("category/<int:itemCategory>/",views.category, name="item_category"),
    path("group/<int:category_sub>/",views.Group_category, name="Group_category"),
    
]