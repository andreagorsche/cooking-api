from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe


class Like(models.Model):
    """
    Like model, related to User and Post
    """
    chef = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = [['chef', 'recipe']]

    def __str__(self):
         return f'{self.chef} {self.recipe}'

