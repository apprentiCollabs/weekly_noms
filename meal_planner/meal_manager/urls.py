from django.conf.urls import url
from .views import AllRecipes, ViewRecipe, MealPlan, DeleteRecipe, EditRecipe, AddRecipe, AddIngredient


urlpatterns = [
    url(r'^all_recipes/$', AllRecipes.as_view(), name='all_recipes'),
    url(r'^edit/(?P<pk>[0-9]+)/$', EditRecipe.as_view(), name='edit_recipe'),
    url(r'^add/$', AddRecipe.as_view(), name='add_recipe'),
    url(r'^ingredient/$', AddIngredient.as_view(), name='add_ingredient'),
    url(r'^detail/(?P<pk>[0-9]+)/$', ViewRecipe.as_view(), name='view_recipe'),
    url(r'^delete/(?P<pk>[0-9]+)/$', DeleteRecipe.as_view(), name='delete_recipe'),
    url(r'^plan/$', MealPlan.as_view(), name='plan'),
]
