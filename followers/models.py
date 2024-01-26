from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Follower model, related to 'follower' and 'followed'.
    'owner/following' is a User that is following another owner.
    'followed' is a User that is followed by a owner aka 'follower'.
    """
    owner = models.ForeignKey(
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
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'