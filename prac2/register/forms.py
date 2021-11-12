from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email  = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    # create new user
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
    def clean(self):
        super(RegisterForm, self).clean()
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            self._errors['username'] = self.error_class(['Username must be at least 3 characters long'])
        return self.cleaned_data
        


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

