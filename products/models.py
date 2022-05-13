from django.db import models
# Create your models here

class Category_group(models.Model):
    title=models.CharField( max_length=100)

    def __str__(self):
        return self.title

class Sub_category(models.Model):
    title=models.CharField( max_length=100)
    group=models.ForeignKey(Category_group, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_group(self):
        return self.group.title
    
class Product(models.Model):
    category=models.ForeignKey(Sub_category, on_delete=models.CASCADE)
    product_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="Item_image/")
    price=models.FloatField()
    discount=models.FloatField()
    actual_price=models.FloatField()
    brand=models.CharField( max_length=100)
    model_name=models.CharField( max_length=100)
    qty=models.IntegerField(default=0)
    desc=models.TextField()
    review_count=models.IntegerField(default=0)
    rating_count=models.FloatField(default=0)

    def __str__(self):
        return self.product_name

class Reviews(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    email=models.CharField(max_length=50)
    name=models.CharField( max_length=50)
    rating=models.IntegerField(default=0)
    review=models.TextField()
    comment=models.CharField( max_length=200)
    date=models.DateField( auto_now_add=True)
    time=models.TimeField( auto_now_add=True)
    helpfull=models.IntegerField(default=0)

    class Meta:
        ordering=['time']

    def __str__(self):
        return self.product.product_name

class Other_image(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="Item_image/")

    def __str__(self):
        return self.product.product_name

class SSD(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    ssd=models.IntegerField()

    def __str__(self):
        return self.product.product_name

class RAM(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    ram=models.IntegerField()

    def __str__(self):
        return self.product.product_name

class ROM(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    rom=models.IntegerField()

    def __str__(self):
        return self.product.product_name

class Display_desc(models.Model):
    product=models.OneToOneField(Product,on_delete=models.CASCADE)
    desc=models.TextField()

    def __str__(self):
        return self.product.product_name

class Display_size(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    size=models.CharField(max_length=200)

    def __str__(self):
        return self.product.product_name

class Battery_power(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    power=models.IntegerField()

    def __str__(self):
        return self.product.product_name

class Battery_desc(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    desc=models.TextField()
    def __str__(self):
        return self.product.product_name

class Camera_front(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    front=models.CharField( max_length=50)

    def __str__(self):
        return self.product.product_name

class Camera_rear(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    rear=models.CharField( max_length=50)
    def __str__(self):
        return self.product.product_name

class Camera_desc(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    desc=models.TextField()
    
    def __str__(self):
        return self.product.product_name

class OS(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    os=models.CharField( max_length=100)

    def __str__(self):
        return self.product.product_name

class Connectivity_technologies(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    desc=models.CharField( max_length=200)

    def __str__(self):
        return self.product.product_name

class Special_features(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    desc=models.TextField()

    def __str__(self):
        return self.product.product_name

class BOX(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    desc=models.TextField()

    def __str__(self):
        return self.product.product_name

class Manufacturer(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    desc=models.CharField( max_length=100)

    def __str__(self):
        return self.product.product_name

class Country_of_origin(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    country=models.CharField( max_length=100)

    def __str__(self):
        return self.product.product_name

class Item_weight(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    weight=models.CharField( max_length=50)

    def __str__(self):
        return self.product.product_name

