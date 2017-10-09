from django.views.generic import CreateView
from django.contrib.auth.models import User, Permission
from django.shortcuts import render

# Create your views here.
class RegisterUser(CreateView):
    model = User
    fields = ['username', 'password']