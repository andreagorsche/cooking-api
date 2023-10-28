from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Rating, Recipe, Comment
from recipes.serializers import RecipeSerializer
from comments.serializers import CommentSerializer
 

class RatingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True) 
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all())
    comment = CommentSerializer(read_only=True, required=False)  # Embed the CommentSerializer

    class Meta:
        model = Rating
        fields = ['id', 'user', 'recipe', 'comment', 'stars']
