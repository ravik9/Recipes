from django.contrib import admin
from .models import Recipe, Ingredient, Step

admin.site.register(Step)
admin.site.register(Ingredient)
admin.site.register(Recipe)
