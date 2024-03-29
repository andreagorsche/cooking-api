from rest_framework import generics, permissions, filters
from cooking_api.permissions import IsOwnerOrReadOnly
from .models import Rating
from recipes.models import Recipe
from .serializers import RatingSerializer
from rest_framework.exceptions import ValidationError


class RatingList(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        owner = self.request.user
        return Rating.objects.select_related('recipe').all()

    def perform_create(self, serializer):
        owner = self.request.user
        recipe_id = self.request.data.get('recipe')
        stars = self.request.data.get('stars')

        if stars:
            recipe = Recipe.objects.exclude(owner=self.request.user).get(pk=recipe_id)  # Fetch recipe not owned by the user
            serializer.save(owner=self.request.user, recipe=recipe)
        else:
            raise ValidationError("A star rating is required.")

        
class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a rating, if you are logged in update an owned rating
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
