from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    date_of_creation = models.DateField(auto_now_add=True)
    date_of_modification = models.DateField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return "Title %s created by %s" %(self.title,self.author.name)
