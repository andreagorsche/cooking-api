from rest_framework import generics, permissions
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
from cooking_api.permissions import IsChefOrReadOnly

class RecipeList(generics.ListCreateAPIView):
    """
    List all recipes, if logged create your own recipe
    """
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Recipe.objects.all()

    def perform_create(self, serializer):
        serializer.save(recipe=self.request.user)

class RecipeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve recipe, if logged in update and delete your own recipe
    """
    permission_classes = [IsChefOrReadOnly]
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()