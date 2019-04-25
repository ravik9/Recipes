from django.urls import path
from django.conf.urls import url
from .views import RecipeView, UserView, SpecificRecipeView, RecipesbyUser


urlpatterns = [
    path('recipeapi/', RecipeView.as_view()),
    path('users/', UserView.as_view()),
    url(r'recipeapi/(?P<id>\d+)/$', SpecificRecipeView.as_view()),
    url(r'recipesbyuser/(?P<id>\d+)/$', RecipesbyUser)
]
