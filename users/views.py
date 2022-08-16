from urllib.parse import urlencode
from django.shortcuts import render
from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, ListView, View
from users.forms import RegisterUser, LoginForm
from  users.models import Profile
from django.urls import reverse_lazy, reverse

class NewUser(CreateView):
    template_name = "users/register.html"
    form_class = RegisterUser
    success_url = reverse_lazy("users:login")
