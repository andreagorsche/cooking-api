from rest_framework import generics, permissions
from cooking_api.permissions import IsOwnerOrReadOnly, IsNotOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer, MarkCommentInappropriateSerializer

class CommentList(generics.ListCreateAPIView):
    """
    List comments, if logged in create a comment
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def get_queryset(self):
        queryset = Comment.objects.all()
        recipe_id = self.request.query_params.get('recipe')
        if recipe_id:
            queryset = queryset.filter(recipe_id=recipe_id)
        return queryset

    def perform_create(self, serializer):
        # Get the recipe_id from the request data
        owner = self.request.user
        recipe_id = self.request.data.get('recipe')
        content = self.request.data.get('content')        
        # Check if recipe_id exists
        if recipe_id:
            # Save the comment with the associated recipe_id
            serializer.save(owner=self.request.user, recipe_id=recipe_id)
            return

        # If recipe_id is not provided, return an error response
        return Response({"error": "recipe_id is required"}, status=status.HTTP_400_BAD_REQUEST)

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
    permission_classes = [IsNotOwnerOrReadOnly]
    queryset = Comment.objects.all()


    def perform_update(self, serializer, **kwargs):
        comment_id = kwargs.get('comment_id')  # Get the comment ID from the URL
        comment = self.get_object()

        # PermissionDenied for comment owner 
        if comment.owner == self.request.user:
            raise PermissionDenied("It is not possible to set your own comment to inappropriate. Please delete your comment if you want to remove it.")
        
        serializer.instance.is_inappropriate = True
        serializer.instance.marked_inappropriate_by = self.request.user
        serializer.save()

        return Response({"message": "Comment marked as inappropriate."}, status=status.HTTP_200_OK)