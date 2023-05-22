from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Recipe(models.Model):
    chef = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50, default='')
    time_effort = models.CharField(max_length=20, default="")
    ingredients = models.TextField(default="")
    description = models.TextField(default="")
    image = models.ImageField(
        upload_to='images/', default='../kitchen-ga12e7dca3_1920_ch64p1'
    )

class Meta:
        ordering = ['-updated_at']

def __str__(self):
    return f"{self.chef}'s recipe"


def create_recipe(sender, instance, created, **kwargs):
    if created:
        Recipe.objects.create(chef=instance)

post_save.connect(create_recipe, sender=User)