"""Models to store data for the generation of meal plans on the fly."""

from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Ingredient(models.Model):
    """Store ingredients for each recipe."""

    name = models.CharField(max_length=100)

    # amount = models.IntegerField()
    # measurement = models.CharField(max_length=10)
    # Fields stripped out for iterative development.
    # TODO: translate ingredients into serialized comma sperated strings in
    #   the recipe model so that we can record name AND amount on a per-recipe
    #   basis.

class Recipe(models.Model):
    """Store recipes for the user."""

    user = models.ForeignKey(
        User,
        related_name='recipes'
    )
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
    tags = TaggableManager()
    title = models.CharField(max_length=100)
    cook_time = models.IntegerField()  # to be stored as an integer number of minutes
    instructions = models.TextField(max_length=1000)
