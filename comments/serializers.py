from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    recipe_id = serializers.ReadOnlyField(source='recipe.id')
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    is_inappropriate = serializers.ReadOnlyField() 

    def get_is_owner (self,obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)
        
    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'profile_id', 'recipe_id', 'created_at', 'updated_at', 
            'content', 'is_owner', 'profile_image','is_inappropriate',
        ]

class CommentDetailSerializer(CommentSerializer):
    recipe_id = serializers.ReadOnlyField(source='recipe.id')

class MarkCommentInappropriateSerializer(serializers.ModelSerializer):
    comment_id = serializers.IntegerField()  # Add this field to identify the comment
    is_inappropriate = serializers.BooleanField() 

    class Meta:
        model = Comment
        fields = ['comment_id', 'is_inappropriate']