from rest_framework import generics, permissions
from cooking_api.permissions import IsChefOrReadOnly
from .models import Like
from likes.serializers import LikeSerializer

class LikeList(generics.ListCreateAPIView):
    """
    List likes, if logged in  create a like.
    """
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(chef=self.request.user)

class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like, if you own it delete a like by id.
    """
    permission_classes = [IsChefOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()