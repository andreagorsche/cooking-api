from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.ReadOnlyField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    saved = serializers.BooleanField()


  
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 5:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 1024:
            raise serializers.ValidationError(
                'Image height larger than 1024px!'
            )
        if value.image.width > 1024:
            raise serializers.ValidationError(
                'Image width larger than 1024px!'
            )
        return value

    def get_is_owner (self,obj):
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = Recipe
        fields = [
            'id', 'owner', 'profile_id', 'image', 'created_at', 'updated_at', 'cuisine', 'title', 'ingredients', 'time_effort',
            'description', 'is_owner', 'saved',
        ]

class MarkAsSavedSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='recipe.id')
    saved = serializers.BooleanField() 

    class Meta:
        model = Recipe
        fields = ['id', 'saved']