from rest_framework import generics, permissions
from cooking_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer, MarkCommentInappropriateSerializer

class CommentList(generics.ListCreateAPIView):
    """
    List comments, if logged in create a comment
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, if you are logged in update or delete an owned comment
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()

class MarkCommentInappropriate(generics.UpdateAPIView):
    """
    Mark a comment as inappropriate.
    """
    queryset = Comment.objects.all()
    serializer_class = MarkCommentInappropriateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.instance.is_inappropriate = True
        serializer.save()