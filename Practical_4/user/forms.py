from django import forms
from django.db.models import fields
from django.forms import TextInput,EmailInput, Textarea,NumberInput,Select, DateInput, widgets
from .models import User,Post

class UserForm(forms.ModelForm):
    class Meta:
        
        fields=('name','email','address','phone','date_of_birth')
        widgets={
            'name':TextInput(attrs={'class':'form-control'}),
            'email':EmailInput(attrs={'class':'form-control'}),
            'address':Textarea(attrs={'class':'form-control'}),
            'phone':TextInput(attrs={'class':'form-control'}),
            'date_of_birth':DateInput(attrs={'class':'form-control'})
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title','content')
        widgets={
            'title':TextInput(attrs={'class':'form-control'}),
            'content':Textarea(attrs={'class':'form-control'})
        }
        