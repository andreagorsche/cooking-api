from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    chef = serializers.ReadOnlyField(source='chef.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'chef', 'image', 'created_at', 'updated_at', 'favorite_cuisine',
            'bio'
        ]