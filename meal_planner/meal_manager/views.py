"""Process recipes into a meal plan."""

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import(
    DetailView, ListView, UpdateView, CreateView, DeleteView,
)
from .models import Recipe, Ingredient

class AllRecipes(ListView):
    """Home view for logged in users."""

    queryset = Recipe.objects.filter(user=reqeuest.user)
    template_name = 'meal_manager/all_recipes.html'


class AddRecipe(CreateView):
    """Edit a single recipe."""
    form_class =  # TODO: model form is imported and goes here
    template_name = 'meal_manager/add.html'
    success_url = reverse_lazy('meals:all_recipes')



class EditRecipe(UpdateView):
    """Edit a single recipe."""
    
    form_class =  # TODO: model form is imported and goes here
    template_name = 'meal_manager/edit.html'
    success_url = reverse_lazy('meals:all_recipes')



class ViewRecipe(DetailView):
    """View a recipe in more complete detail."""
    
    model = Recipe


class DeleteRecipe(DeleteView):
    """Remove an unwanted recipe."""
    
    model = Recipe
    success_url = reverse_lazy('meals:all_recipes')


class MealPlan(ListView):
    """Generate a weighted-random meal plan."""
    
    pass
