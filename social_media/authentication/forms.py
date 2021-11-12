from django import forms
from django.contrib.auth.models import User

class PersonalInfoForm(forms.ModelForm):
  gender_choices = [('M', 'Male'), ('F', 'Female')]
  state_choices = [('gujarat', 'Gujarat'),('maharashtra' ,'Maharashtra')]
  city_choices = {
    'gujarat':[
      ('gandhinagar', 'Gandhinagar'),
      ('ahmedabad', 'Ahmedabad'),
      ('rajkot', 'Rajkot'),
      ('surat', 'Surat')
    ],
    'maharashtra':[
      ('mumbai', 'Mumbai'),
      ('nagpur', 'Nagpur'),
      ('pune', 'Pune'),
      ('nashik', 'Nashik')
    ],
  }    
  
  first_name = forms.CharField(max_length= 128,
    widget= forms.TextInput(attrs={'class':'form-control'})
  )
  last_name = forms.CharField(max_length= 128,
    widget= forms.TextInput(attrs={'class':'form-control'})
  )
  dob = forms.DateField(
    widget=forms.widgets.NumberInput(attrs={
      'type':'date',
      'class':'form-control'
      })
  )
  mobile_no = forms.CharField(
    min_length= 10, max_length= 10,
    widget= forms.TextInput(attrs={'class':'form-control'})
  )
  gender = forms.ChoiceField(
    widget= forms.RadioSelect(attrs={'class':''}),
    choices= gender_choices,
  )
  state = forms.ChoiceField(choices= state_choices,
    widget= forms.Select(attrs={'class':'form-control'}),
  )
  city_choices_flat = []
  for k, v in city_choices.items():
    city_choices_flat.extend(v)
  city = forms.ChoiceField(choices= city_choices_flat,
    widget= forms.Select(attrs={'class':'form-control'}),
  )
  class Meta:
    model = User
    fields = ['first_name', 'last_name']
    # fields = ('first_name', 'last_name', 'dob', 'mobile_no', 'gender', 'city','state', 'pincode')