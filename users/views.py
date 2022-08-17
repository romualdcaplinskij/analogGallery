from django.views.generic import CreateView
from users.forms import RegisterUser
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.shortcuts import redirect


class NewUser(CreateView):
    template_name = "users/register.html"
    form_class = RegisterUser
    success_url = reverse_lazy("users:login")

def logout_user(request):
    logout(request)
    return redirect('/')
