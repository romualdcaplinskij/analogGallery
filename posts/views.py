from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from django.utils import timezone
from .models import Post
from .forms import PostForm

class PostListView(ListView):
    template_name = 'posts/wall.html'
    model = Post
    context_object_name = 'posts'

class PostCreateView(CreateView):
    template_name = 'posts/new_post.html'
    form_class = PostForm
    model = Post
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):
    template_name = "posts\post_detail.html"
    model = Post
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Post, id=id_)