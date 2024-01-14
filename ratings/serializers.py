from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Rating, Recipe, Comment
from recipes.serializers import RecipeSerializer
from django.core.validators import MinValueValidator, MaxValueValidator

class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all(), write_only=True)
    recipe_id = serializers.ReadOnlyField(source='recipe.id')
    recipe_title = serializers.ReadOnlyField(source='recipe.title')
    recipe_description = serializers.ReadOnlyField(source='recipe.description')
    recipe_ingredients = serializers.ReadOnlyField(source='recipe.ingredients')
    stars = serializers.IntegerField(
        validators=[
            MinValueValidator(1, message="Rating should be at least 1."),
            MaxValueValidator(5, message="Rating should be at most 5.")
        ]
    )

    class Meta:
        model = Rating
        fields = ['id', 'owner', 'recipe_id', 'recipe_title','recipe_description','recipe_ingredients', 'recipe','stars']


    def create(self, validated_data):
            # Check if a rating from the same user for the same recipe already exists
            existing_rating = Rating.objects.filter(owner=validated_data['owner'], recipe_id=validated_data['recipe_id']).first()

            if existing_rating:
                # Update the existing rating
                existing_rating.stars = validated_data['stars']
                existing_rating.save()
                return existing_rating
            else:
                # Create a new rating
                return Rating.objects.create(**validated_data)