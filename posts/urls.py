from django.urls import path, include
from posts.views import PostListView, PostCreateView, PostDetailView, UserGallery, DeletePostView


app_name = "posts"

urlpatterns = [
    path('', PostListView.as_view(), name='wall'),
    path('new_post/', PostCreateView.as_view(), name='upload_image'),
    path('post_detail/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('user_gallery/', UserGallery.as_view(), name='user_gallery'),
    path('user_gallery/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
]