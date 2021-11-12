from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.shortcuts import redirect, render

from .forms import RegisterForm,LoginForm
# Create your views here.

def registerUser(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('/home')
        else:
            return render(response,"register.html",{"form":form})
    form = RegisterForm()

    return render(response,"register.html",{"form":form})


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('/home')
        else:
            form = LoginForm()
            return render(request,"login.html",{"form":form,
            'error_message':'Username or password is incorrect'})
            

    form = LoginForm()
    return render(request,"login.html",{"form":form})

def home(req):
    if req.method=='POST':
        print("inside")
        logout(req)
        return redirect('/login')
    return render(req,'home.html')