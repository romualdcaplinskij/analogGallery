from django.urls import path, include
from .views import PostListView

app_name = "posts"

urlpatterns = [
    path('', PostListView.as_view(), name='wall'),
]