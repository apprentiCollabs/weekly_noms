"""Views for user managment."""

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Permission
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView


class Index(TemplateView):
    template_name = "user_manager/index.html"


class RegisterUser(CreateView):
    """Register a user using default model form."""
    model = User
    template_name = "registration/signup.html"
    success_url = reverse_lazy('meals:all_recipes')
    form_class = UserCreationForm
