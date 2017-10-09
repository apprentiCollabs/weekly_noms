"""Views for user managment."""

from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User, Permission
from django.shortcuts import render


class Index(TemplateView):
    template_name = "user_manager/index.html"


class RegisterUser(CreateView):
    """Register a user using default model form."""
    model = User
    fields = ['username', 'password']
