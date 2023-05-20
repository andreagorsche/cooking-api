from rest_framework import generics, permissions
from cooking_api.permissions import IsChefOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

class CommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(chef=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsChefOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()