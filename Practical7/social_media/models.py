from django.db import models
from Auth.models import CustomUser

# Create your models here.

class Post(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    date_of_creation = models.DateField(auto_now_add=True)
    date_of_modification = models.DateField(auto_now=True)
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return self.title+"/"+self.author.username+"/"+self.date_of_creation.strftime("%d-%m-%Y")
