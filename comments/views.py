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

class MarkCommentInappropriate(generics.RetrieveUpdateAPIView):
    """
    Mark a comment as inappropriate.
    """
    serializer_class = MarkCommentInappropriateSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Comment.objects.all()


    def perform_update(self, serializer):
        comment = self.get_object()

        # Check if the user is not the comment owner
        if not self.has_object_permission(self.request, self, comment):
            serializer.instance.is_inappropriate = True
            serializer.save()
        else:
            # PermissionDenied for comment owner 
            raise PermissionDenied("It is not possible to set your own comment to inappropriate. Please delete your comment if you want to remove it.")