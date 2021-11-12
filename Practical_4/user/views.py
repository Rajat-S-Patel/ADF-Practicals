from typing import ContextManager
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post, User
from .forms import PostForm, UserForm
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView 
from django.urls import reverse_lazy

def home(req):
    if req.method == 'GET':
        postform = PostForm()
        posts = Post.objects.all()
        return render(req,'home.html',{'postform':postform,'posts':posts})
    elif req.method == 'POST':
        postform = PostForm(req.POST)
        if postform.is_valid():
            post = postform.save(commit=False)
            post.author = req.user
            postform.save()
            return render(req,'home.html',{'postform':postform})
        else:
            return render(req,'home.html',{'postform':postform})

class userCreate(CreateView):
    model = User
    form_class=UserForm
    template_name="usercreate.html"
    context_object_name ="users"
    success_url = reverse_lazy('user-list')

class userDetail(DetailView): 
    model = User
    template_name="userdetail.html"
    context_object_name ="users"

class userUpdate(UpdateView): 
    model = User
    form_class=UserForm
    template_name="userupdate.html"
    context_object_name ="users"
    success_url = reverse_lazy('user-list')

class userDelete(DeleteView): 
    model = User
    template_name="userdelete.html"
    context_object_name ="users"
    success_url = reverse_lazy('user-list')

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