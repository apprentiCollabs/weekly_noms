from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
import factory
from faker import Faker
from django.core.urlresolvers import reverse_lazy


class UserFactory(factory.django.DjangoModelFactory):
    """Make users for auth testing."""

    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user_number_{}".format(n))


class UserTestCases(TestCase):
    """Test user login and registration."""

    def setUp(Self):
        self.client = Client()
        self.request = RequestFactory()

    def test_user_login(self):
        new_user = UserFactory.create()
        new_user.username = "username"
        new_user.set_password("nicks_potatos")
        new_user.save()
        response = self.client.post("/login/", {
            "username": new_user.username
            "password": "nicks_potatos"
        })
        self.assertTrue(request.user.is_authenticated)
        # self.assertRedirects(response, '')
    
    def test_user_register(self):
        """Test that user registration view works."""
        self.assertTrue(User.object.count() == 0)
        self.client.post("/register/", {
            "username": "noperope"
            "password": "welldone"
            "check_password": "welldone"
        })
        self.assertTrue(User.objects.count == 1)

    def test_new_user_no_recipes(self):
        """Test that a new user won't have recipes associated."""
        self.assertTrue(User.object.count() == 0)
        self.client.post("/register/", {
            "username": "noperope"
            "password": "welldone"
            "check_password": "welldone"
        })
        self.assertTrue(User.objects.get(username="noperope").recipes.count() == 0)