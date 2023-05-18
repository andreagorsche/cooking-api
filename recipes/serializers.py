from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    chef = serializers.ReadOnlyField(source='chef.username')
    is_chef = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='chef.profile.image.url')
  
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

    def get_is_chef (self,obj):
        request = self.context['request']
        return request.user == obj.chef
    
    class Meta:
        model = Recipe
        fields = [
            'id', 'chef', 'profile_id', 'image', 'created_at', 'updated_at', 'title', 'ingredients', 'time_effort',
            'description', 'is_chef', 'profile_image'
        ]