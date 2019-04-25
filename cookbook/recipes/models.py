from django.contrib.auth.models import User
from django.db import models


class Recipe(models.Model):
    name = models.CharField(blank=False, max_length=300)
    recipe_owner = models.OneToOneField(User, on_delete=models.CASCADE)


class Step(models.Model):
    step_text = models.CharField(blank=False, max_length=300)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class Ingredient(models.Model):
    text = models.CharField(blank=False, max_length=300)
    recipe_ing_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)



