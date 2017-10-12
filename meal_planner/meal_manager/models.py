"""Models to store data for the generation of meal plans on the fly."""

from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


class Ingredient(models.Model):
    """Store ingredients for each recipe."""

    name = models.CharField(max_length=100)


class Recipe(models.Model):
    """Store recipes for the user."""

    user = models.ForeignKey(
        User,
        related_name='recipes'
    )
    ingredients = models.ManyToManyField(
        'Ingredient',
        related_name='recipes',
        blank=True
    )
    tags = TaggableManager(blank=True)
    title = models.CharField(max_length=100)
    # to be stored as an integer number of minutes
    cook_time = models.IntegerField()
    instructions = models.TextField(max_length=1000)
