from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
  
    class Meta:
        model = Like
        fields = [
            'id', 'owner', 'recipe', 'created_at',
        ]
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'this like may be a duplicate'
            })