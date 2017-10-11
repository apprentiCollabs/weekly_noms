from django.test import TestCase

from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.contrib import auth
import factory
from faker import Faker
from django.core.urlresolvers import reverse_lazy


class UserFactory(factory.django.DjangoModelFactory):
    """Make users for auth testing."""

    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user_number_{}".format(n))


class MealTestCases(TestCase):
    """Test recipe creation and editing plus meal plan generation."""

    def setUp(self):
        self.client = Client()
        self.request = RequestFactory()