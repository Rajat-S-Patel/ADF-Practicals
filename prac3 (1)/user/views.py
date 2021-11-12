from django.shortcuts import render
from .models import user_details

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView 
from django.urls import reverse_lazy


class userCreate(CreateView): 
    model = user_details
    fields = '__all__'
    template_name="usercreate.html"
    context_object_name ="users"
    success_url = reverse_lazy('userlist')

class userList(ListView): 
    model = user_details
    template_name="userlist.html"
    context_object_name ="users"

class userDetail(DetailView): 
    model = user_details
    template_name="userdetail.html"
    context_object_name ="users"

class userUpdate(UpdateView): 
    model = user_details
    fields = '__all__'
    template_name="userupdate.html"
    context_object_name ="users"
    success_url = reverse_lazy('userlist')


class userDelete(DeleteView): 
    model = user_details
    template_name="userdelete.html"
    context_object_name ="users"
    success_url = reverse_lazy('userlist')
