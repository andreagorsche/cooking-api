from rest_framework import generics, permissions
from cooking_api.permissions import IsChefOrReadOnly
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer

class RecipeList(generics.ListCreateAPIView):
    """
    List all recipes, if logged create your own recipe
    """
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Recipe.objects.all()

    """
    Associate the recipe with the logged in chef
    """

    def perform_create(self, serializer):
        serializer.save(chef=self.request.user)

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve recipe, if logged in update and delete your own recipe
    """
    serializer_class = RecipeSerializer
    permission_classes = [IsChefOrReadOnly]
    queryset = Recipe.objects.all()