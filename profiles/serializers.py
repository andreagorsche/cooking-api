from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    chef = serializers.ReadOnlyField(source='chef.username')
    is_chef = serializers.SerializerMethodField()

    def get_is_chef (self,obj):
        request = self.context['request']
        return request.user == obj.chef

    class Meta:
        model = Profile
        fields = [
            'id', 'chef', 'image', 'created_at', 'updated_at', 'favorite_cuisine',
            'bio', 'is_chef'
        ]