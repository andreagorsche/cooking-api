from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from comments.models import Comment

@receiver(post_save, sender=Comment)
def update_inappropriate_comments_count(sender, instance, **kwargs):
    user = instance.owner
    profile = Profile.objects.get(owner=user)

    # Check if the comment is marked as inappropriate
    if instance.is_inappropriate:
        profile.inappropriate_comments_count += 1
        profile.save()

        # Check if the count exceeds 5 and set the profile as inactive
        if profile.inappropriate_comments_count >= 5:
            profile.is_active = False
            profile.save()