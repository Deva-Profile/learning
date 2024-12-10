from django.db import models

import uuid


class Userlogin(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=100,null=True,blank=True)
    phone_number=models.IntegerField(default=0,null=True,blank=True)
    address = models.TextField(null = True,blank = True)
    email = models.EmailField(unique=True) 

    def __str__(self):
        return f"{self.name} --- {self.id}"


class Category(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits = 10,decimal_places = 2 ,default=0.00,null = True,blank = True)
    stock = models.IntegerField(default=0, null=True, blank=True)
    image = models.URLField(max_length=500, blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"{self.name}==={self.id}"

class Cart(models.Model):
    id = id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(Userlogin, on_delete=models.SET_NULL,null=True)
    products = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return f"{self.products}"

class CartItem(models.Model):
    id = id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.cart} --- {self.id}"


class Order(models.Model):
    id = id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(Userlogin, on_delete=models.SET_NULL,null=True)
    products = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    order_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} --- {self.order_at} --- {self.id} "

class OrderItem(models.Model):
    id = id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.order} --- {self.id}"
    

class Article(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    lastedit_date = models.DateTimeField(null=True) 

    def get_absolute_url(self): 
        return "/p/%i/" % self.id



