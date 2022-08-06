from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostForm

class PostListView(ListView):
    template_name = 'posts/wall.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'

class PostCreateView(CreateView):
    template_name = 'posts/new_post.html'
    form_class = PostForm
    queryset = Post.objects.all()
    # context_object_name = 'posts'
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.author = self.request.user
        return super().form_valid(form)