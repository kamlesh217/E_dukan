from django.urls import path
from . import views

app_name='seller'

urlpatterns = [
    path('seller/', views.seller, name="profile"  ),
]