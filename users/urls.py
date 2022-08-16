from django.urls import path
from users.views import NewUser
from django.contrib.auth.views import LoginView, PasswordResetView



app_name = "users"

urlpatterns = [
    path('register/', NewUser.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('password_reset/', PasswordResetView.as_view(), name="password_reset"),
]