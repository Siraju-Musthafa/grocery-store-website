from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class catogarytable(models.Model):
    catogaryname=models.CharField(max_length=100,null=True)
    catogaryimage=models.ImageField(upload_to='media',null=True)
    catogarystatus=models.CharField(max_length=30,null=True)
    
   
class brandstable(models.Model):
       brandname=models.CharField(max_length=100,null=True)
       brandimage=models.ImageField(upload_to='media',null=True)
       brandstatus=models.CharField(max_length=30,null=True)
   
class productstable(models.Model):
       name=models.CharField(max_length=100,null=True)
       image=models.ImageField(upload_to='media',null=True)
       description=models.CharField(max_length=100,null=True)
       status=models.CharField(max_length=30,null=True)
       brand=models.ForeignKey(brandstable,on_delete=models.CASCADE,null=True)
       our_price=models.FloatField(null=True)
       orginal_price=models.FloatField(null=True)
       tax_amount=models.FloatField(null=True)
       open_stock=models.FloatField(null=True)
       current_stock=models.FloatField(null=True)
       catogary=models.ForeignKey(catogarytable,on_delete=models.CASCADE,null=True)
       


class enquiries(models.Model):
      Name=models.CharField(max_length=100,null=True)
      email=models.EmailField(null=True)
      message=models.CharField(max_length=100,null=True)



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(productstable, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    def total_price(self):
        return self.product.our_price * self.quantity
      


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Cart)
    total_amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Pending")
    oid=models.CharField(max_length=100,null=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class orderupdates(models.Model):
     orderid=models.IntegerField(null=True)
     updatedesc=models.CharField(max_length=100,null=100)
     timestamp=models.DateField(auto_now_add=True)
     amount=models.IntegerField(null=True)
     paymentid=models.CharField(max_length=50,null=True)