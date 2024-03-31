from rest_framework import generics, permissions, filters
from cooking_api.permissions import IsOwnerOrReadOnly
from .models import Rating
from recipes.models import Recipe
from .serializers import RatingSerializer
from rest_framework.exceptions import ValidationError
from django.db.models import Avg


class RatingList(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = Rating.objects.all()
        recipe_id = self.request.query_params.get('recipe')
        if recipe_id:
            queryset = queryset.filter(recipe_id=recipe_id)
        return queryset

    def calculate_average_rating(self, queryset):
        average_rating = queryset.aggregate(Avg('stars'))['stars__avg']
        if average_rating is not None:
            return round(average_rating, 1)
        return 0  # Return 0 if there are no ratings

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        average_rating = self.calculate_average_rating(queryset)
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        owner = self.request.user
        recipe_id = self.request.data.get('recipe')
        stars = self.request.data.get('stars')

        if stars:
            recipe = Recipe.objects.exclude(owner=self.request.user)\
                      .get(pk=recipe_id)
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
