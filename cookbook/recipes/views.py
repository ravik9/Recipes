from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Recipe
from .Serializer import RecipeSerializer, UserSerializer
from django.shortcuts import get_object_or_404


@api_view(['Get'])
def RecipesbyUser(request, id):
    recipes = Recipe.objects.filter(recipe_owner=id)
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)



class RecipeView(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpecificRecipeView(APIView):
    def get(self, request, id):
        recipes = get_object_or_404(Recipe, pk=id)
        serializer = RecipeSerializer(recipes)
        return Response(serializer.data)

    def delete(self, request, pk=id):
        receipes = get_object_or_404(Recipe, pk=id)
        receipes.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        recipe = get_object_or_404(Recipe, pk=id)
        if request.data.get("name") is not None:
            recipe.name = request.data.get("name")
        if request.data.get("recipe_owner") is not None:
            recipe.recipe_owner = request.data.get("recipe_owner")
        recipe.save()
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


