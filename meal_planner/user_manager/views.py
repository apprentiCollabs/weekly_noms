"""Views for user managment."""

from django.views.generic import CreateView
from django.contrib.auth.models import User, Permission
from django.shortcuts import render


class RegisterUser(CreateView):
    """Register a user using default model form."""
    model = User
    fields = ['username', 'password']
