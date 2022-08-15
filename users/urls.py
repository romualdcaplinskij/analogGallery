from django.urls import path, include
from users.views import NewUser, Login


app_name = "users"

urlpatterns = [
    path('register/', NewUser.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
]