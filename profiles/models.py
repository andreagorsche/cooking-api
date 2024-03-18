from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from cooking_api.constants import CUISINE_CHOICES
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_uhncwe.jpg'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bio = models.CharField(max_length=200, default="")
    favorite_cuisine = models.CharField(max_length=13, choices=CUISINE_CHOICES, default='none')
    inappropriate_comments_count = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.owner}'s profile"

    @property
    def owner_profile_image(self):
        return self.owner.profile.image.url if hasattr(self.owner, 'profile') else None

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)

@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    if instance.owner:
        instance.owner.delete()