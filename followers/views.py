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

class FollowerDetail(generics.RetrieveDestroyAPIView):
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
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer

    def get_queryset(self):
        # Filter the queryset based on the follower_id in the URL
        follower_id = self.kwargs['pk']
        return Follower.objects.filter(id=follower_id)