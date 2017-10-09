from django.conf.urls import url
from .views import AllRecipes, EditRecipe, ViewRecipe, MealPlan


urlpatterns = [
    url(r'^all_recipes/$', AllRecipes.as_view(), name='all_recipes'),
    url(r'^all_recipes/edit/$', EditRecipe.as_view(), name='edit_recipes'),
    url(r'^all_recipes/detail/$', ViewRecipe.as_view(), name='view_recipe'),
    url(r'^all_recipes/delete/(?P<pk>[0-p]+)/$', ViewRecipe.as_view(), name='view_recipe'),
    url(r'^plan/$', MealPlan.as_view(), name='plan'),
]
