from rest_framework import generics
from profiles.models import Profile
from profiles.serializers import ProfileSerializer
from cooking_api.permissions import IsChefOrReadOnly


class ProfileList(generics.ListCreateAPIView):
    """
    List all profiles
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve, update and delete a profile
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer