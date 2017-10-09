from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(
        User,
        related_name='recipes'
    )
    tags = TaggableManager()
    title = models.CharField(max_length=100)
    instructions = models.TextField(max_length=1000)

class Ingredient(models.Model):
    recipes = models.ManyToManyField(
        Recipe,
        related_name='ingredients'
    )
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    measurement = models.CharField(max_length=10)