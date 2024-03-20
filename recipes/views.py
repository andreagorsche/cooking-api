from rest_framework import generics, permissions, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from cooking_api.permissions import IsOwnerOrReadOnly
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


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
        'owner__followed__owner__profile', # user feed
        'owner__profile', # user posts
        'cuisine', # posts filtered by cuisine
        
    ]
    search_fields = [
        'owner__username',
        'title',
        'description',
        'ingredients',
    ]
    
    """
    order recipes by created_at
    """
    queryset = Recipe.objects.all().order_by('-created_at')

    """
    Filter specific ingredients
    """
    def get_queryset(self):
        # Check if 'ingredients' query parameter is provided
        ingredients_var = self.request.query_params.get('ingredients')
        queryset = Recipe.objects.all()

        if ingredients_var:
            # Split the ingredients into a list
            ingredients_list = ingredients_var.split(',')
            # Filter recipes that contain any of the specified ingredients
            for ingredient in ingredients_list:
                queryset = queryset.filter(ingredients__icontains=ingredient)
        return queryset
  
    """
    Associate the recipe with the logged in chef
    """
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve recipe, if logged in update and delete your own recipe
    """
    serializer_class = RecipeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Recipe.objects.all()

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user

        if instance.saved_by.filter(pk=user.pk).exists():
            # If the user has already saved the recipe, remove it from saved recipes
            instance.saved_by.remove(user)
            saved = False
        else:
            # Otherwise, save the recipe for the user
            instance.saved_by.add(user)
            saved = True

        return Response({"saved": saved}, status=status.HTTP_200_OK)
