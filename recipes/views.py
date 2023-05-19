from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
from cooking_api.permissions import IsChefOrReadOnly

class RecipeList(APIView):
    serializer_class = RecipeSerializer
    permission_classes = [IsChefOrReadOnly]

    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(
            recipes, many=True, context={'request': request}
            )
        return Response(serializer.data)

class RecipeDetail(APIView):
    serializer_class = RecipeSerializer
    permission_classes = [IsChefOrReadOnly]

    def get_object(self, pk):
        try:
            recipe = Recipe.objects.get(pk=pk)
            self.check_object_permissions(self.request, recipe)
            return recipe
        except Recipe.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(
            recipe, context={'request': request}
            )
        return Response(serializer.data)

    def put(self, request, pk):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)