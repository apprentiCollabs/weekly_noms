from django.db import models
from django.forms import ModelForm


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['tags', 'title', 'ingredients', 'instructions']
