from email.mime import image
from multiprocessing import context
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from posts.models import Post
from posts.forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(ListView):
    template_name = "posts/wall.html"
    model = Post
    context_object_name = "posts"

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new_post.html"
    form_class = PostForm
    model = Post
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = "posts\post_detail.html"
    model = Post
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Post, id=id_)



class UserGallery(LoginRequiredMixin, ListView):
    login_url = 'users:login'
    template_name = "posts/user_gallery.html"
    model = Post
    context_object_name = "gallery"


    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)



