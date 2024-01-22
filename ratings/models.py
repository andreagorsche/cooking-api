from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe
from comments.models import Comment

from django.core.validators import MaxValueValidator

class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    comment = models.ForeignKey (Comment, on_delete=models.CASCADE, null=True,blank=True, default=None)
    stars = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(5)])

    def __str__(self):
        return f"{self.owner.username} rated {self.recipe} with {self.stars} stars"

    class Meta:
        ordering = ['-stars']