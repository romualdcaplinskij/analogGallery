# from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from users.forms import RegisterUser
from  users.models import Profile
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class NewUser(CreateView):
    template_name = "users/register.html"
    form_class = RegisterUser
    success_url = reverse_lazy("users:login")
