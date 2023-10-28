from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Rating, Recipe, Comment

from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(read_only=True)  # Embed the RecipeSerializer
    comment = CommentSerializer(read_only=True, required=False)  # Embed the CommentSerializer

    def create(self, validated_data):
        # Extract 'comment' and 'stars' data
        comment_data = validated_data.pop('comment', None)
        recipe = validated_data.pop('recipe') 

        # Create a new Rating object with 'stars'
        rating = Rating.objects.create(stars=stars, **validated_data)

        if comment_data:
            comment = Comment.objects.create(**comment_data)
            validated_data['comment'] = comment  # Associate the comment with the rating

        # Since 'recipe' is a required field for a rating
        validated_data['recipe'] = recipe  # Associate the recipe with the rating

        return Rating.objects.create(**validated_data)

    class Meta:
        model = Rating
        fields = ['id', 'user', 'recipe', 'comment', 'stars']
