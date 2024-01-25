from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    email = serializers.ReadOnlyField(source='owner.email')
    bio = serializers.CharField(max_length=200)
    is_owner = serializers.SerializerMethodField()
    followed_id = serializers.SerializerMethodField()
    recipes_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()


    def validate_image(self, value):
        if value.size > 1024 * 1024 * 5:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 1024:
            raise serializers.ValidationError(
                'Image height larger than 1024px!'
            )
        if value.image.width > 1024:
            raise serializers.ValidationError(
                'Image width larger than 1024px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_followed_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            followed = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return followed.id if followed else None
        return None
    

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'email', 'created_at', 'updated_at', 'image', 'is_owner', 'followed_id',
            'recipes_count', 'followers_count', 'following_count', 'inappropriate_comments_count',
            'is_active', 'bio', 'favorite_cuisine'
        ]