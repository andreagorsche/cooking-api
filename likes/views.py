from rest_framework import generics, permissions
from cooking_api.permissions import IsChefOrReadOnly
from .models import Like
from .serializers import LikeSerializer

class LikeList(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(chef=self.request.user)

class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsChefOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()