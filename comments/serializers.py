from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    chef = serializers.ReadOnlyField(source='chef.username')
    is_chef = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='chef.profile.id')
    profile_image = serializers.ReadOnlyField(source='chef.profile.image.url')

    def get_is_chef (self,obj):
        request = self.context['request']
        return request.user == obj.chef
    
    class Meta:
        model = Comment
        fields = [
            'id', 'chef', 'profile_id', 'recipe', 'created_at', 'updated_at', 
            'content', 'is_chef', 'profile_image',
        ]

class CommentDetailSerializer(CommentSerializer):
    recipe = serializers.ReadOnlyField(source='recipe.id')

  