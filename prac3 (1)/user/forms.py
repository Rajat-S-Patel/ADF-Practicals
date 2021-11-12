from django import forms
from .models import user_details

class userForm(forms.ModelForm):
    class Meta:
        model = user_details
        fields = '__all__'