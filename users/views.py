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
    success_url = reverse_lazy("login")


class Login(ListView):
    template_name = "users/login.html"
    form_class = LoginForm
    model = Profile
    
    # def get(self, request):
    #     form = self.form_class
    #     return render(request, self.template_name, {form:form})

    # def post(self, request):

    #     pass

# def logout_view(request):
#     logout(request)
