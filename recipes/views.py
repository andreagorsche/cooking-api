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

    def post(self, request):
        serializer_class = PostSerializer
        permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
        serializer = RecipeSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(chef=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )