from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Recipe
from .serializers import RecipeSerializer


class RecipeList(APIView):
    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(
            posts, many=True, context={'request': request}
        )
        return Response(serializer.data)