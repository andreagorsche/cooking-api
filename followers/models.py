from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model, related to 'follower' and 'followed_chef'.
    'follower' is a User that is following a User.
    'followed_chef' is a User that is followed by 'follower'.
    """
    follower = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed_chef = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['follower', 'followed_chef']

    def __str__(self):
        return f'{self.follower} {self.followed_chef}'