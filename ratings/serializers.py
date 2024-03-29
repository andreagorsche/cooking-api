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

    class Meta:
        model = Rating
        fields = ['id', 'owner', 'recipe', 'stars']
