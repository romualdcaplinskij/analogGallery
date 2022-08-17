from django.urls import path, include
from posts.views import PostListView, PostCreateView, PostDetailView, UserGallery


app_name = "posts"

urlpatterns = [
    path('', PostListView.as_view(), name='wall'),
    path('new_post/', PostCreateView.as_view(), name='upload image'),
    path('<int:id>', PostDetailView.as_view(), name='post detail'),
    path('user_gallery/', UserGallery.as_view(), name='user_gallery'),
]