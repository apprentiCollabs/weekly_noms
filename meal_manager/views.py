"""Process recipes into a meal plan."""

from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    DetailView, ListView, UpdateView, CreateView, DeleteView,
)
from .models import Recipe
from .forms import RecipeForm, IngredientForm


class AllRecipes(LoginRequiredMixin, ListView):
    """Home view for logged in users."""

    template_name = 'meal_manager/all_recipes.html'
    login_url = reverse_lazy('users:login')

    def get_queryset(self):
        """Return recipes belonging to the current user only."""
        return Recipe.objects.filter(user=self.request.user)


class AddRecipe(LoginRequiredMixin, CreateView):
    """Edit a single recipe."""

    login_url = reverse_lazy('users:login')
    form_class = RecipeForm
    template_name = 'meal_manager/add.html'
    success_url = reverse_lazy('meals:all_recipes')

    def form_valid(self, form):
        """Add user information to form data."""
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)


class AddIngredient(LoginRequiredMixin, CreateView):
    """Add a new ingredient object to the database."""

    login_url = reverse_lazy('users:login')
    form_class = IngredientForm
    template_name = 'meal_manager/ingredient.html'
    success_url = reverse_lazy('meals:add_recipe')


class EditRecipe(LoginRequiredMixin, UpdateView):
    """Edit a single recipe."""

    login_url = reverse_lazy('users:login')
    model = Recipe
    form_class = RecipeForm
    template_name = 'meal_manager/edit.html'
    success_url = reverse_lazy('meals:all_recipes')


class ViewRecipe(LoginRequiredMixin, DetailView):
    """View a recipe in more complete detail."""

    login_url = reverse_lazy('users:login')
    model = Recipe
    template_name = 'meal_manager/recipe.html'


class DeleteRecipe(LoginRequiredMixin, DeleteView):
    """Remove an unwanted recipe."""

    login_url = reverse_lazy('users:login')
    model = Recipe
    success_url = reverse_lazy('meals:all_recipes')


class MealPlan(LoginRequiredMixin, ListView):
    """Generate a weighted-random meal plan."""

    login_url = reverse_lazy('users:login')
    template_name = 'meal_manager/plan.html'

    def get_queryset(self):
        """Get recipes for the meal plan."""
        return Recipe.objects.filter(user=self.request.user).order_by('?')[:7]
