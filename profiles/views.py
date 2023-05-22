from rest_framework import generics
from cooking_api.permissions import IsChefOrReadOnly
from profiles.models import Profile
from profiles.serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve and update the profile you own
    """
    permission_classes = [IsChefOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer