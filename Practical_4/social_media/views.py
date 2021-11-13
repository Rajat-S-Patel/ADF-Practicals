from typing import ContextManager
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView 
from django.urls import reverse_lazy

def home(request):
    form = PostForm()
    context={}
    context['form']=form
    posts = Post.objects.all()
    context['posts']=posts
    return render(request, 'home.html', context)


class postCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name="post-create.html"
    context_object_name="posts"
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class postList(ListView):
    model=Post
    template_name="post-list.html"
    context_object_name="posts"

class postDetail(DetailView):
    model=Post
    template_name="post-detail.html"
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