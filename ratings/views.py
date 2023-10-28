from rest_framework import generics, permissions, filters
from cooking_api.permissions import IsOwnerOrReadOnly
from .models import Rating
from .serializers import RatingSerializer

class RatingList(generics.ListCreateAPIView):
    """
    List all ratings, if logged create your own ratings
    """
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Rating.objects.all()
    
    def perform_create(self, serializer):
        user = self.request.user
        recipe_id = self.request.data.get('recipe')  # Assuming 'recipe' field is sent in the POST request
        recipe = Recipe.objects.get(pk=recipe_id)
        
        # Extract comment data if available in the request
        comment_data = self.request.data.get('comment', None)

        # Create the rating associated with the recipe
        rating = serializer.save(user=user, recipe=recipe)

        if comment_data:
            # Create a comment associated with the rating and the provided comment data
            Comment.objects.create(rating=rating, user=user, text=comment_data)
        
class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a rating, if you are logged in update or delete an owned comment
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()