from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Rating, Recipe, Comment
from recipes.serializers import RecipeSerializer
from comments.serializers import CommentSerializer
 
from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all(), write_only=True)
    recipe_id = serializers.ReadOnlyField(source='recipe.id')
    recipe_title = serializers.ReadOnlyField(source='recipe.title')
    recipe_description = serializers.ReadOnlyField(source='recipe.description')
    recipe_ingredients = serializers.ReadOnlyField(source='recipe.ingredients')

    class Meta:
        model = Rating
        fields = ['id', 'owner', 'recipe_id', 'recipe_title','recipe_description','recipe_ingredients', 'recipe','stars']

