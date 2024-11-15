from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    career = models.CharField(max_length=200)