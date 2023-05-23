from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
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
    filter_backends = [
        filters.SearchFilter,
         DjangoFilterBackend,
    ]
    filterset_fields = [
        'chef__followed__chef__profile', # user feed
        'likes__chef__profile', # posts a user liked
        'chef__profile', # user posts
        'chef__recipe__cuisine' # posts filtered by cuisine
    ]
    search_fields = [
        'chef__username',
        'title',
        'description'
    ]

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