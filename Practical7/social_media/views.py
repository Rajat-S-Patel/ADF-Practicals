from django.shortcuts import redirect, render

# Create your views here.
from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
def home(request):
    form = PostForm()
    context={}
    context['form']=form
    posts = Post.objects.all()
    context['posts']=posts
    return render(request, 'home.html', context)


class postCreate(CreateView,LoginRequiredMixin):
    model = Post
    form_class = PostForm
    template_name="post-create.html"
    context_object_name="posts"
    success_url=reverse_lazy('home')
    login_url=reverse_lazy('signin')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class postList(ListView):
    model=Post
    template_name="post-list.html"
    context_object_name="posts"

class postDetail(LoginRequiredMixin,DetailView):
    model=Post
    template_name="post-detail.html"
    context_object_name="posts"
    login_url=reverse_lazy('signin')


class postUpdate(LoginRequiredMixin,UpdateView): 
    model = Post
    form_class=PostForm
    template_name="post-edit.html"
    context_object_name ="posts"
    login_url=reverse_lazy('signin')

    def dispatch(self, request,*args,**kwargs):
        obj:Post = self.get_object()
        if obj.author.username != self.request.user.username and self.request.user.is_superuser == False:
            return render(request, 'forbidden.html', {'msg': 'You are not allowed to edit this post'}) 
        
        else:
            return super().dispatch(request,*args,**kwargs)
            

    def get_success_url(self) -> str:
        return reverse_lazy('post-detail', kwargs={'pk': self.object.id})

class postDelete(LoginRequiredMixin,DeleteView):
    model = Post
    context_object_name="posts"
    success_url=reverse_lazy('home')
    login_url = reverse_lazy('signup')

    def get(self, request, *args, **kwargs):
        return self.post(args, kwargs)

    def dispatch(self, request,*args,**kwargs):
        obj:Post = self.get_object()
        if obj.author.username != self.request.user.username and self.request.user.is_superuser == False:
            return render(request, 'forbidden.html', {'msg': 'You are not allowed to delete this post'}) 
        else:
            return super().dispatch(request,*args,**kwargs)
    
