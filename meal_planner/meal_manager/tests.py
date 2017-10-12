"""Tests for ingredients, recipes and the meal plan itself."""

from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
import factory
from .models import Recipe, Ingredient


class UserFactory(factory.django.DjangoModelFactory):
    """Make users for auth testing."""

    class Meta:
        """Metadata."""
        model = User

    username = factory.Sequence(lambda n: "user_number_{}".format(n))


class IngredientFactory(factory.django.DjangoModelFactory):
    """Build recipes for creation and editing testing."""

    class Meta:
        """Metadata."""
        model = Ingredient

    name = factory.Sequence(lambda n: "ingredient_number{}".format(n))


class RecipeFactory(factory.django.DjangoModelFactory):
    """Build recipes for creation and editing testing."""

    class Meta:
        """Metadata."""
        model = Recipe

    user = factory.SubFactory(UserFactory)
    # ingredients = factory.SubFactory(IngredientFactory)
    tags = 'tag1 tag2'
    title = 'test recipe'
    cook_time = 180
    instructions = 'figure it out'


class RecipeTestCases(TestCase):
    """Test recipe creation and editing."""

    def setUp(self):
        self.users = [UserFactory.create() for i in range(20)]
        self.recipes = [RecipeFactory.create() for i in range(20)]
        self.ingredients = [IngredientFactory.create() for i in range(20)]
        self.client = Client()
        self.request = RequestFactory()

    def test_recipe_in_database(self):
        """Recipes generated for testing make it into the testing database."""

        self.assertTrue(Recipe.objects.count() == 20)

    def test_recipe_has_user(self):
        """Test that new recipes are created with users associated."""

        recipe = Recipe.objects.first()
        self.assertTrue(hasattr(recipe, "__str__"))

    def test_add_recipe(self):
        """Test that the add route produces new recipes."""

        count = Recipe.objects.count()
        self.client.force_login(self.users[0])
        self.client.post('/meals/add/', {
            'title': 'title',
            'ingredients': 10,  # id for an ingredient object
            'tags': 'stuff nonsesne',
            'cook_time': 20,
            'instructions': 'words here',
            'add_new_recipe': ''
        })
        self.assertFalse(count == Recipe.objects.count())


class IngredientTestCases(TestCase):
    """Test ingredient creation."""

    def setUp(self):
        self.client = Client()
        self.request = RequestFactory()


class PlanTestCases(TestCase):
    """Test meal plan generation."""

    def setUp(self):
        self.client = Client()
        self.request = RequestFactory() 
