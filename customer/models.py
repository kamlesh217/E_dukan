from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    customer=models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField(max_length=15)
    address=models.CharField( max_length=100)
    city=models.CharField( max_length=100)
    state=models.CharField( max_length=100)
    zip=models.IntegerField()

    def __str__(self):
        return f"{self.customer.first_name}   {self.customer.last_name}"


