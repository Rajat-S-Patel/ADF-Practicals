from django.db import models

# Create your models here.

class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=1000)
    phone = models.CharField(max_length=10)
    age=models.IntegerField()
    gender = models.CharField(max_length=10,default='1',choices=(('M','Male'),('F','Female'),('O','Other')))
    