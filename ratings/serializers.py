from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    owner_id = serializers.ReadOnlyField(source='owner.id')
    recipe_id = serializers.ReadOnlyField(source='recipe.id')
    stars = serializers.IntegerField(
        validators=[
            MinValueValidator(1, message="Rating should be at least 1."),
            MaxValueValidator(5, message="Rating should be at most 5.")
        ]
    )

    class Meta:
        model = Rating
        fields = ['id', 'owner_id', 'recipe_id', 'stars']

    def create(self, validated_data):
        owner_id = validated_data['owner_id']
        recipe = validated_data['recipe']

        existing_rating = Rating.objects.filter(owner_id=owner_id, recipe=recipe).first()

        if existing_rating:
            existing_rating.stars = validated_data['stars']
            existing_rating.save()
            return existing_rating
        else:
            return Rating.objects.create(owner_id=owner_id, **validated_data)
