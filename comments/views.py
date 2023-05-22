from rest_framework import generics, permissions
from cooking_api.permissions import IsChefOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

class CommentList(generics.ListCreateAPIView):
    """
    List comments, if logged in create a comment
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(chef=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, if you are logged in update or delete an owned comment
    """
    permission_classes = [IsChefOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()