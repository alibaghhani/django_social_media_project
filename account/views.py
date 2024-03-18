from django.shortcuts import render
from django.views.generic import CreateView
from .models import User

# Create your views here.
class SignupView(CreateView):
    model = User
    fields = ['username','password','phone_number','biography','hobbies','gender']
    template_name = 'signup.html'
    context_object_name = 'user'
