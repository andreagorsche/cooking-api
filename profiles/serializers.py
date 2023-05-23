from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    chef = serializers.ReadOnlyField(source='chef.username')
    is_chef = serializers.SerializerMethodField()
    profile_image = serializers.ReadOnlyField(source='chef.profile.image.url')
    recipes_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
  
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
        model = Profile
        fields = [
            'id', 'chef', 'image', 'created_at', 'updated_at','bio', 
            'is_chef', 'profile_image', 'recipes_count', 'followers_count', 'following_count'
        ]