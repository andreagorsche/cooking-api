from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    follower = serializers.ReadOnlyField(source='follower.username')
    followed_chef = serializers.ReadOnlyField(source='followed_chef.username')
    
    class Meta:
        model = Follower
        fields = [
            'id', 'follower', 'followed_chef', 'created_at',
        ]
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'you may already follow this chef'
            })