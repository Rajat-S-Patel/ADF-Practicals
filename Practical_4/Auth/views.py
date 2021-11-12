from django import http
from django.shortcuts import redirect, render,HttpResponse
from django.views.generic.edit import UpdateView

from Auth.models import Profile
# from django.contrib.auth.forms import UserCreationForm
from .forms import PersonalInfoForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage, send_mail
from Practical_4 import settings
from django.views.generic import CreateView
from . tokens import generate_token
from django.urls import reverse_lazy

# Create your views here.


def index(req):
    return render(req,'index.html')

def home(req):
    return render(req,'home.html')

def signup(req):
    if req.method == 'POST':
        username = req.POST['username']
        email = req.POST['email']
        pass1 = req.POST['password1']
        pass2 = req.POST['password2']

        if User.objects.filter(username=username):
            messages.error(req,'Username already exists!!')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.error(req,'Email already registered, please use different email.')
            return redirect('signup')

        elif pass1!=pass2:
            messages.error(req,"Password and Confirm password doesn't match ")
            return redirect('signup')
        
        user = User.objects.create_user(username=username,email=email,password = pass1)
        user.is_active = False
        user.save()

        messages.success(req,"Your account is successfully created!!! Please check your email to confirm your email address in order to activate your account.")

        subject="Confirm Email for NewGen Social Media"
        current_site=get_current_site(req)
        msg = render_to_string('email_confirm.html',{
            'name':user.username,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)
        })
        email = EmailMessage(
            subject,
            msg,
            settings.EMAIL_HOST_USER,
            [user.email],
        )
        email.fail_silently=True
        email.send()

        return redirect('signin')

    else:
        return render(req,'signup.html')

def signin(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(req, user)
            return redirect('personalinfo-update',pk=Profile.objects.get(user=user).id)
        else:
            messages.error(req, "Bad Credentials!!")
            return redirect('signin')

    return render(req,"signin.html")

def activate(req,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None

    if user is not None and generate_token.check_token(user,token):
        user.is_active = True
        user.save()
        login(req,user)
        messages.success(req, "Congratulations!!, Your Account has been activated!!")
        return redirect('personalinfo',pk=user.id)
    else:
        messages.error(req,'activation failed !!')
        return redirect('signup')


def signout(req):
    logout(req)
    messages.success(req,'Logout sucessfully')
    return redirect('index')

class PersonalInfo(CreateView):
    model=Profile
    form_class=PersonalInfoForm
    template_name='personal_info.html'
    context_object_name='user'
    success_url=reverse_lazy('signin')

    def get_initial(self):
        return {'user':self.request.user}

class PersonalInfoUpdate(UpdateView):
    model=Profile
    form_class=PersonalInfoForm
    template_name='personal_info.html'
    context_object_name='user'
    success_url=reverse_lazy('signin')

    def get_initial(self):
        return {'user':self.request.user}