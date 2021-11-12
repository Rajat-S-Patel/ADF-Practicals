from typing import ContextManager
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post, User
from .forms import PostForm, UserForm
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView 
from django.urls import reverse_lazy

class postCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name="postcreate.html"
    context_object_name="posts"
    success_url=reverse_lazy('post-list')

class postList(ListView):
    model=Post
    template_name="postlist.html"
    context_object_name="posts"

class postDetail(DetailView):
    model=Post
    template_name="postdetail.html"
    context_object_name="posts"

class postUpdate(UpdateView): 
    model = Post
    form_class=PostForm
    template_name="postupdate.html"
    context_object_name ="posts"
    success_url = reverse_lazy('post-list')

class postDelete(DeleteView):
    model=Post
    template_name="postdelete.html"
    context_object_name="users"
    success_url=reverse_lazy("post-list")