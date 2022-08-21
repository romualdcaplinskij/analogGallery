from django.urls import path
from . import views
from posts.views import PostListView, PostCreateView, PostDetailView, UserGallery, DeletePostView, Editor


app_name = "posts"

urlpatterns = [
    path('', PostListView.as_view(), name='wall'),
    path('new_post/', PostCreateView.as_view(), name='upload_image'),
    path('post_detail/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('user_gallery/', UserGallery.as_view(), name='user_gallery'),
    path('user_gallery/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('editor/<int:pk>', Editor.as_view(), name="editor")
]