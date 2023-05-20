from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    chef = serializers.ReadOnlyField(source='chef.username')
    
    class Meta:
        model = Like
        fields = [
            'id', 'chef', 'recipe', 'created_at',
        ]
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'this like may be a duplicate'
            })