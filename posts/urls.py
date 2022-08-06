from django.urls import path, include
from .views import PostListView, PostCreateView

app_name = "posts"

urlpatterns = [
    path('', PostListView.as_view(), name='wall'),
    path('new_post/', PostCreateView.as_view(), name='upload_image')
]