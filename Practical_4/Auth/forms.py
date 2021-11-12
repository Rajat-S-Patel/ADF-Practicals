from django import forms
from django.contrib.auth.models import User
from django.forms import fields

from .models import CustomUser

class UserForm(forms.ModelForm):
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

    date_of_birth=forms.DateField(
        widget=forms.DateInput(attrs={
            'class':'form-control'
        })
    )
    state= forms.ChoiceField(
        widget=forms.Select(attrs={'class':'form-select'}),
        choices=STATE_CHOICE
    )
    gender=forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=GENDER_CHOICE
    )
    city = forms.ChoiceField(choices=CITY_CHOICE,
        widget=forms.Select(attrs={'class':'form-select'}),
    )
    image = forms.ImageField(label='Profile Image',required=True)
    resume = forms.FileField(label='Resume',required=True)
    
    class Meta:
        model = CustomUser
        fields=['date_of_birth','state','gender','city','image','resume']