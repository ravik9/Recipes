from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Recipe, Ingredient

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = 'id', 'name', 'recipe_owner'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        exclude= []

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude=[]