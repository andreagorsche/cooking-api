from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    chef = serializers.ReadOnlyField(source='chef.username')
    
    class Meta:
        model = Like
        fields = [
            'id', 'chef', 'recipe', 'created_at',
        ]