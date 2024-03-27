from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from cooking_api.constants import CUISINE_CHOICES

class Recipe(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50, default='')
    cuisine = models.CharField(max_length=13, choices=CUISINE_CHOICES, default='american')
    time_effort = models.CharField(max_length=20, default="")
    ingredients = models.TextField(default="")
    description = models.TextField(default="")
    image = models.ImageField(
        upload_to='images/', default=None
    )


    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f'{self.id} {self.title}'