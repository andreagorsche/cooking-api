from rest_framework import generics, permissions, filters
from cooking_api.permissions import IsOwnerOrReadOnly
from .models import Rating
from recipes.models import Recipe
from .serializers import RatingSerializer
from rest_framework.exceptions import ValidationError

class RatingList(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        owner = self.request.user
        return Rating.objects.select_related('recipe').all() # Fetch ratings

    def perform_create(self, serializer):
        owner = self.request.user
        recipe_id = serializer.validated_data.get('recipe_id')
        stars = serializer.validated_data.get('stars')
        
        # Check if the user has already rated the recipe
        existing_rating = Rating.objects.filter(owner=owner, recipe_id=recipe_id).first()
        if existing_rating:
            raise ValidationError("You can only rate a recipe once. If you want to change the rating you made, please feel free to update it.")
        
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