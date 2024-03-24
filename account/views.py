from django.contrib.auth.views import LoginView as Login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import User

# Create your views here.
class SignupView(CreateView):
    model = User
    fields = ['username','password','phone_number','biography','hobbies','gender']
    template_name = 'signup.html'
    context_object_name = 'user'
    success_url = reverse_lazy('signup')

class SigninView(Login):
    model = User
    success_url = reverse_lazy('signup')
    template_name = 'signin.html'