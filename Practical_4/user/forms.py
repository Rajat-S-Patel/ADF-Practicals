from django import forms
from django.db.models import fields
from django.forms import TextInput,EmailInput, Textarea,NumberInput,Select, DateInput, widgets
from .models import User,Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=('title','content')
        widgets={
            'title':TextInput(attrs={'class':'form-control'}),
            'content':Textarea(attrs={'class':'form-control'})
        }
        