from rest_framework import generics, permissions
from cooking_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer

class FollowerList(generics.ListCreateAPIView):
    """
    List all followers, if logged in follow other users
    """
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)

class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    If logged in follow and unfollow a chef
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()