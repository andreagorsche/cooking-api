from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    """
    Recipe model, related to 'chef'(User instance).
    """
    chef = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
     image = models.ImageField(
        upload_to='images/', default='../kitchen-ga12e7dca3_1920_ch64p1', blank=True
    cooking_time = models.CharField(blank=True)
    ingredients = models.TextField(blank=True)
    description = models.TextField(blank=True)
    )

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f'{self.id} {self.title}'
