from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_id = serializers.ReadOnlyField(source='followed.id')
    
    class Meta:
        model = Follower
        fields = [
            'id', 'owner', 'followed', 'created_at', 'followed_id'
        ]
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'you may already follow this chef'
            })