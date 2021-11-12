from django.shortcuts import render
from .models import UserDetails
from .forms import UserForm
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView 
from django.urls import reverse_lazy


class userCreate(CreateView): 
    model = UserDetails
    form_class=UserForm
    template_name="usercreate.html"
    context_object_name ="users"
    success_url = reverse_lazy('user-list')

class userList(ListView): 
    model = UserDetails
    template_name="userlist.html"
    context_object_name ="users"

class userDetail(DetailView): 
    model = UserDetails
    template_name="userdetail.html"
    context_object_name ="users"

class userUpdate(UpdateView): 
    model = UserDetails
    form_class=UserForm
    template_name="userupdate.html"
    context_object_name ="users"
    success_url = reverse_lazy('user-list')


class userDelete(DeleteView): 
    model = UserDetails
    template_name="userdelete.html"
    context_object_name ="users"
    success_url = reverse_lazy('user-list')
