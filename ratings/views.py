from rest_framework import generics, permissions, filters
from cooking_api.permissions import IsOwnerOrReadOnly
from .models import Rating
from recipes.models import Recipe
from .serializers import RatingSerializer

class RatingList(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Recipe.objects.exclude(owner=user)  # Fetch recipes not owned by the user

    def perform_create(self, serializer):
        user = self.request.user
        recipe_id = self.request.data.get('recipe')
        stars = self.request.data.get('stars')

        if stars:
            recipe = Recipe.objects.exclude(owner=user).get(pk=recipe_id)  # Fetch recipe not owned by the user
            serializer.save(user=user, recipe=recipe)
        else:
            raise ValidationError("A star rating is required.")

        
class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a rating, if you are logged in update or delete an owned comment
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()