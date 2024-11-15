from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
