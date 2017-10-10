from django.db import models
from django.forms import ModelForm
from .models import Recipe


class RecipeForm(ModelForm):
    """Form for adding and editing new recipies."""

    class Meta:
        model = Recipe
        fields = ['tags', 'title', 'ingredients', 'instructions']
