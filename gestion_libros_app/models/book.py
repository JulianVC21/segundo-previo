from django.db import models
import uuid

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    realease_date = models.DateField()
    isbn = models.IntegerField(unique=True)
    