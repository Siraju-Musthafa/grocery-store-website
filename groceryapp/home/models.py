from django.db import models


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