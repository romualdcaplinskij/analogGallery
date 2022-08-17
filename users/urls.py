from django.urls import path
from users.views import NewUser
from django.contrib.auth.views import LoginView, PasswordResetView, LogoutView
from users.views import logout_user



app_name = "users"

urlpatterns = [
    path('register/', NewUser.as_view(), name="register"),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path('password_reset/', PasswordResetView.as_view(), name="password_reset"),
    path('logout', logout_user, name='logout'),
]