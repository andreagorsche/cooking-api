from rest_framework import generics, permissions, filters
from cooking_api.permissions import IsOwnerOrReadOnly
from .models import Rating
from recipes.models import Recipe
from .serializers import RatingSerializer

class RatingList(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        owner = self.request.user
        return Rating.objects.all()  # Fetch ratings

    def perform_create(self, serializer):
        owner = self.request.user
        recipe_id = self.request.data.get('recipe')
        stars = self.request.data.get('stars')

        if stars:
            recipe = Recipe.objects.exclude(owner=user).get(pk=recipe_id)  # Fetch recipe not owned by the user
            serializer.save(owner=user, recipe=recipe)
        else:
            raise ValidationError("A star rating is required.")

        
class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a rating, if you are logged in update or delete an owned comment
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()