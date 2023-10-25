from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    is_inappropriate = serializers.BooleanField() 

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
            'id', 'owner', 'profile_id', 'recipe', 'created_at', 'updated_at', 
            'content', 'is_owner', 'profile_image','is_inappropriate',
        ]

class CommentDetailSerializer(CommentSerializer):
    recipe = serializers.ReadOnlyField(source='recipe.id')

class MarkCommentInappropriateSerializer(serializers.ModelSerializer):
    content = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField(source='owner.username')
    is_inappropriate = serializers.BooleanField() 
    marked_inappropriate_by = serializers.ReadOnlyField(source='marked_inappropriate_by.username')

    class Meta:
        model = Comment
        fields = [
            'owner', 'content', 'is_inappropriate', 'marked_inappropriate_by'
            ]
    