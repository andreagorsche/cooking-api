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
        serializer.save(owner=self.request.user)

class FollowerDetail(generics.RetrieveAPIView):
    """
    If logged in follow a chef
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

class UnfollowUserView(generics.DestroyAPIView):
    """
    If logged in, unfollow a chef.
    """
    lookup_field = 'followed_id' 
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer

    def get_queryset(self):
        # Filter the queryset based on the followed_id in the URL
        followed_id = self.kwargs['followed_id']
        return Follower.objects.filter(id=followed_id)