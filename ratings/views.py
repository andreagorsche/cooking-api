from rest_framework import generics, permissions, filters
from cooking_api.permissions import IsOwnerOrReadOnly
from .models import Rating
from .serializers import RatingSerializer, RatingDetailSerializer

class RatingList(generics.ListCreateAPIView):
    """
    List all ratings, if logged create your own ratings
    """
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Rating.objects.all()

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a rating, if you are logged in update or delete an owned comment
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingDetailSerializer
    queryset = Rating.objects.all()