from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from social_media import settings
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from .tokens import generate_taken
from django.views.generic import UpdateView
from .forms import PersonalInfoForm
from django.urls import reverse_lazy

def index(request):
  return render(request, 'index.html')

def signup(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if User.objects.filter(username=username).exists():
      messages.error(request, 'Username already registered!')
      return redirect('signup')

    if User.objects.filter(email=email).exists():
      messages.error(request, 'Email already registered!')
      return redirect('signup')
    
    if password1 != password2:
      messages.error(request, "Passwords doesn't match")
      return redirect('signup')

    user = User.objects.create_user(username=username,email=email, password=password1)
    user.is_active = False
    user.save()

    messages.success(request, 'Your account is created successfuly! Check your mail inbox to activate your account')

    current_site = get_current_site(request)
    email_subject = 'Confirm your Email @ Social Media'
    email_messaage = render_to_string('confirm_email.html', {
      'username':user.username,
      'domain':current_site.domain,
      'uid':urlsafe_base64_encode(force_bytes(user.pk)),
      'token':generate_taken.make_token(user)
    })
    email = EmailMessage(
      email_subject, 
      email_messaage,
      settings.EMAIL_HOST_USER,
      [user.email]
    )
    email.fail_silently = True
    email.send()

    return redirect('signin')
  return render(request, 'signup.html')

def activate(request, uidb64, token):
  try:
    user_id = force_text(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk = user_id)
  except (TypeError, User.DoesNotExist, ValueError, OverflowError):
    user = None

  if user.is_active:
    messages.info(request, 'Your account has already been activated')
    return redirect('signin')
  if user is not None and generate_taken.check_token(user, token):
    user.is_active = True
    user.save()
    login(request, user)
    messages.success(request, "Congrats! Your account has been activated")
    return redirect('add_personal_info', pk = user.id)

def signin(request):
  if request.method == 'POST':
    username_email = request.POST['username_email']
    password = request.POST['password']

    user = authenticate(username = username_email, password = password)
    if user is None:
      user = authenticate(email = username_email, password = password)

    if user is not None:
      login(request, user)
      return render(request, 'index.html', {"first_name":user.first_name})
    else:
      messages.error(request, 'Invalid Credentials!')
      return redirect('signin')
  return render(request, 'signin.html')

def signout(request):
  logout(request)
  messages.success(request, 'Logged out Successfully!')
  return redirect('home')

class PersonalInfo(UpdateView):
  model = User
  form_class = PersonalInfoForm
  template_name = 'add_personal_info.html'
  context_object_name = 'user'
  success_url = reverse_lazy('signin')