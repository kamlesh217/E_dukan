from products.models import *
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Cart(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.ForeignKey(User, on_delete=models.CASCADE)
    qty=models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.customer.first_name
    
    def get_total(self):
        return self.qty* self.product.price


class Wishlist(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.customer.first_name
    