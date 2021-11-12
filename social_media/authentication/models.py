from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=gender_choices)
    birth_date = models.DateField(null=True)
    profile_picture = models.ImageField(upload_to='dps')

    def __str__(self):
        return self.user.first_name + self.user.last_name
