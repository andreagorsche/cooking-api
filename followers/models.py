from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model, related to 'follower' and 'followed_chef'.
    'follower' is a User that is following another Chef.
    'followed_chef' is a User that is followed by a chef aka 'follower'.
    """
    chef = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    """
    'unique_together' makes sure a user can't the same user twice.
    """

    class Meta:
        ordering = ['-created_at']
        unique_together = ['chef', 'followed']

    def __str__(self):
        return f'{self.chef} {self.followed}'