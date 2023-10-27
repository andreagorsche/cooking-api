from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe
from django.core.validators import MaxValueValidator

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(5)])

    def __str__(self):
        return f"{self.user.username} rated {self.post.title} with {self.stars} stars"

    class Meta:
        ordering = ['-stars']