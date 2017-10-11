from django.test import TestCase

from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.contrib import auth
import factory
from faker import Faker
from django.core.urlresolvers import reverse_lazy
from .models import Recipe, Ingredient


class UserFactory(factory.django.DjangoModelFactory):
    """Make users for auth testing."""

    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user_number_{}".format(n))


class IngredientFactory(factory.django.DjangoModelFactory):
    """Build recipes for creation and editing testing."""

    class Meta:
        model = Ingredient

    name = factory.Sequence(lambda n: "ingredient_number{}".format(n))


class RecipeFactory(factory.django.DjangoModelFactory):
    """Build recipes for creation and editing testing."""

    class Meta:
        model = Recipe

    user = factory.SubFactory(UserFactory)
    ingredients = factory.SubFactory(IngredientFactory)
    tags = 'tag1 tag2'
    title = 'test recipe'
    cook_time = 180
    instructions = 'figure it out'


class RecipeTestCases(TestCase):
    """Test recipe creation and editing."""

    def setUp(self):
        self.users = [UserFactory.create() for i in range(20)]
        self.recipes = [RecipeFactory.create() for i in range(20)]


    def test_add_recipe(self):
        self.assertTrue(Recipe.objects.count() == 0)



class IngredientTestCases(TestCase):
    """Test ingredient creation."""

    def setUp(self):
        self.client = Client()
        self.request = RequestFactory()

    # def 


class PlanTestCases(TestCase):
    """Test meal plan generation."""

    def setUp(self):
        self.client = Client()
        self.request = RequestFactory()

    # def 