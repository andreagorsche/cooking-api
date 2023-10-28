from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Rating, Recipe, Comment
from recipes.serializers import RecipeSerializer
from comments.serializers import CommentSerializer
 
from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all(), write_only=True)

    class Meta:
        model = Rating
        fields = ['id', 'owner', 'recipe', 'stars']

