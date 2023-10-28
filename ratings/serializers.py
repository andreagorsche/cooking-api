from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Rating, Recipe, Comment

from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all())
    comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), required=False, allow_null=True)
    stars = serializers.IntegerField(min_value=0, max_value=5, required=True)

    def create(self, validated_data):
        # Extract 'comment' and 'stars' data
        comment_data = validated_data.pop('comment', None)
        stars = validated_data.pop('stars')

        # Create a new Rating object with 'stars'
        rating = Rating.objects.create(stars=stars, **validated_data)

        # If a 'comment' is provided, create a comment associated with the rating
        if comment_data:
            Comment.objects.create(rating=rating, **comment_data)

        return rating

    class Meta:
        model = Rating
        fields = ['id', 'user', 'recipe', 'comment', 'stars']
