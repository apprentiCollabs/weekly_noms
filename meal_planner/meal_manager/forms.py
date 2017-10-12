from django.db import models
from django.forms import ModelForm
from .models import Recipe, Ingredient


class RecipeForm(ModelForm):
    """Form for adding and editing new recipies."""

    class Meta:
        model = Recipe
        fields = ['tags', 'cook_time', 'title', 'ingredients', 'instructions']


class IngredientForm(ModelForm):
    """Form for adding ingredients."""

    class Meta:
        model = Ingredient
        fields = ['name']