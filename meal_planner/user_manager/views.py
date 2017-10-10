"""Views for user managment."""

from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Permission
from django.shortcuts import render, redirect


class Index(TemplateView):
    template_name = "user_manager/index.html"


class RegisterUser(CreateView):
    """Register a user using default model form."""
    model = User
    fields = ['username', 'password']

# NOTE: so what I'd planned to do was write the signup this way. Obviously not a class-based view and tbh, I'm not totally sure what needs to be done to turn it into one. Perhaps a conversation/brief discussion?
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('meals:all_recipes')
#         else:
#             form = UserCreationForm()
#             return render(request, '../registration/signup.html', {'form': form})
