from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.FloatField()
    
class Transaction(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)