from django.conf.urls import url
from .views import AllRecipes, ViewRecipe, MealPlan, DeleteRecipe
#  EditRecipe, AddREcipe

urlpatterns = [
    url(r'^all_recipes/$', AllRecipes.as_view(), name='all_recipes'),
    # url(r'^all_recipes/edit/$', EditRecipe.as_view(), name='edit_recipe'),
    # url(r'^all_recipes/add/$', AddRecipe.as_view(), name='add_recipe'),
    url(r'^all_recipes/detail/(?P<pk>[0-9]+)/$', ViewRecipe.as_view(), name='view_recipe'),
    url(r'^all_recipes/delete/(?P<pk>[0-9]+)/$', DeleteRecipe.as_view(), name='view_recipe'),
    url(r'^plan/$', MealPlan.as_view(), name='plan'),
]
