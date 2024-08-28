from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)

class Customer(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE,related_name='customer')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models. TextField()
    document = models.FileField(upload_to='media/')

class Seller(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE,related_name='seller')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models. TextField()

class Feedback(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    date = models.DateField(auto_now=True)
    feedback = models.TextField()
    reply = models.CharField(max_length=300, null=True, blank=True)


class SellerFeedback(models.Model):
    user = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='seller')
    date = models.DateField(auto_now=True)
    feedback = models.TextField()
    reply = models.CharField(max_length=300, null=True, blank=True)

class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='product')
    document = models.FileField(upload_to='media/')
    name = models.CharField(max_length=100)
    details = models.TextField()
    price = models.CharField(max_length=100)
    count = models.IntegerField()
    status = models.BooleanField(default=0)

class AddToCart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customerid')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productid')
    cart_status = models.BooleanField(default=0)

class BuyNow(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='userid')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_id')
    quantity = models.IntegerField(default=1)
    totalprice = models.IntegerField()
    buynow_status = models.BooleanField(default=0)
    address=models.TextField()
    phone=models.CharField(max_length=10)
    post=models.CharField(max_length=6)

class Payment(models.Model):
    buynowProduct=models.ForeignKey(BuyNow, on_delete=models.CASCADE, related_name='buynow')
    cardnumber = models.CharField(max_length=19)
    cvv = models.CharField(max_length=3)
    expiry_date = models.CharField(max_length=7)

