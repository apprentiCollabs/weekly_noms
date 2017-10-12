from django.db import models
from django.forms import ModelForm, widgets
from .models import Recipe, Ingredient


class RecipeForm(ModelForm):
    """Form for adding and editing new recipies."""

    class Meta:
        model = Recipe
        fields = ['tags', 'cook_time', 'title', 'ingredients', 'instructions']
        widgets = {
            'tags': widgets.CheckboxSelectMultiple,
        }


class IngredientForm(ModelForm):
    """Form for adding ingredients."""

    class Meta:
        model = Ingredient
        fields = ['name']
