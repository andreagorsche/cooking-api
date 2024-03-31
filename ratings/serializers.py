from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Rating, Recipe


class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    stars = serializers.IntegerField(
        validators=[
            MinValueValidator(1, message="Rating should be at least 1."),
            MaxValueValidator(5, message="Rating should be at most 5.")
        ]
    )
    average_rating = serializers.SerializerMethodField()

    def get_average_rating(self, rating):
        queryset = Rating.objects.filter(recipe=rating.recipe)
        average_rating = queryset.aggregate(Avg('stars'))['stars__avg']
        return round(average_rating, 1) if average_rating is not None else 0

    class Meta:
        model = Rating
        fields = ['id', 'owner', 'recipe', 'stars', 'average_rating']
