from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Rating, Recipe

class RatingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    recipe_id = serializers.ReadOnlyField(source='recipe.id') 
    stars = serializers.IntegerField(
        validators=[
            MinValueValidator(1, message="Rating should be at least 1."),
            MaxValueValidator(5, message="Rating should be at most 5.")
        ]
    )

    class Meta:
        model = Rating
        fields = ['id', 'owner', 'recipe_id', 'stars']  
    def create(self, validated_data):
        owner = self.context['request'].user
        recipe_id = self.context['recipe_id'] 

        existing_rating = Rating.objects.filter(owner=owner, recipe_id=recipe_id).first()

        if existing_rating:
            existing_rating.stars = validated_data['stars']
            existing_rating.save()
            return existing_rating
        else:
            return Rating.objects.create(owner=owner, **validated_data)
