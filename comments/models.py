from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe


class Comment(models.Model):
    """
    Comment model, related to User and Post
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, 
        related_name='comments'
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    is_inappropriate = models.BooleanField(
        default=False
    )
    marked_inappropriate_by = models.ForeignKey(User, on_delete=models.SET_NULL, 
        null=True, blank=True, related_name='marked_comments'
    )

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.content

