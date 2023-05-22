from django.db.models import Count
from rest_framework import generics, filters
from cooking_api.permissions import IsChefOrReadOnly
from profiles.models import Profile
from profiles.serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles
    """
    queryset = Profile.objects.annotate(
        recipes_count=Count('chef__recipe', distinct=True),
        followers_count=Count('chef__followed', distinct=True),
        following_count=Count('chef__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'recipes_count',
        'followers_count',
        'following_count',
    ]

class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve and update the profile you own
    """
    permission_classes = [IsChefOrReadOnly]
    queryset = Profile.objects.annotate(
        recipes_count=Count('chef__recipe', distinct=True),
        followers_count=Count('chef__followed', distinct=True),
        following_count=Count('chef__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer