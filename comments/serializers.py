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

    def get_is_owner (self,obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        # Check if the comment is marked as inappropriate, and exclude it from serialization
        if instance.is_inappropriate:
            data['content'] = "This comment has been marked as inappropriate and is hidden."
        
        return data
    
    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'profile_id', 'recipe', 'created_at', 'updated_at', 
            'content', 'is_owner', 'profile_image',
        ]

class CommentDetailSerializer(CommentSerializer):
    recipe = serializers.ReadOnlyField(source='recipe.id')

class MarkCommentInappropriateSerializer(serializers.ModelSerializer):
    is_inappropriate = serializers.ReadOnlyField(source='comments.is_inappropriate')
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
            model = Comment
            fields = [
                'id', 'owner', 'profile_id', 'created_at', 'updated_at', 
                'is_owner', 'profile_image', 'is_inappropriate'
            ]
    