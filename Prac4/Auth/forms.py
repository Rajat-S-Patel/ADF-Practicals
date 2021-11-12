from django import forms
from django.contrib.auth.models import User
from django.forms import fields

class PersonalInfoForm(forms.ModelForm):
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

    first_name = forms.CharField(max_length=50,
                widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50,
                widget=forms.TextInput(attrs={'class':'form-control'}))
    date_of_birth=forms.DateField(
        widget=forms.DateInput(attrs={
            'class':'form-control'
        })
    )
    mobile_no = forms.CharField(min_length=10,max_length=10,
     widget= forms.TextInput(attrs={'class':'form-control'})
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
    
    class Meta:
        model = User
        fields=['first_name','last_name']