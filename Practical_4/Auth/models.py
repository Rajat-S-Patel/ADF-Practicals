from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    GENDER_CHOICE = [('M','Male'),('F','Female'),('O','Other')]
    STATE_CHOICE = [('gujarat','Gujarat'),('rajasthan','Rajasthan'),('maharashtra','Maharashtra')]
    CITY_CHOICE = {
        ('gandhinagar','Gandhinagar'),
        ('ahmedabad','Ahmedabad'),
        ('vadodara','Vadodara'),
        ('surat','Surat'),
        ('jaipur','Jaipur'),
        ('udaipur','Udaipur'),
        ('jodhpur','Jodhpur'),
        ('mumbai','Mumbai'),
        ('pune','Pune'),
        ('nagpur','Nagpur')
    }

    user=models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth=models.DateField()
    mobile_no = models.CharField(max_length=10)
    state= models.CharField(max_length=50,choices=STATE_CHOICE)
    gender=models.CharField(max_length=50,choices=GENDER_CHOICE)
    city = models.CharField(max_length=50,choices=CITY_CHOICE)
    image=models.ImageField(upload_to='profile_photos/',default='profile_photos/default.jpg')
    resume = models.FileField(upload_to='resume/',default='resume/default.pdf')

    def __str__(self) -> str:
        return self.first_name+' '+self.last_name