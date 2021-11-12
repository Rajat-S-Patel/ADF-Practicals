from django import forms
from django.db.models import fields
from django.forms import TextInput,EmailInput, Textarea,NumberInput,Select
from .models import UserDetails

class UserForm(forms.ModelForm):

    class Meta:
        model = UserDetails
        fields=('name','email','address','phone','age','gender')
        widgets={
            'name':TextInput(attrs={'class':'form-control'}),
            'email':EmailInput(attrs={'class':'form-control'}),
            'address':Textarea(attrs={'class':'form-control'}),
            'phone':TextInput(attrs={'class':'form-control'}),
            'age':NumberInput(attrs={'class':'form-control'}),
            'gender':Select(attrs={'class':'form-control'})
        }