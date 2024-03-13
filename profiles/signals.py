from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from comments.models import Comment
import os
from django.core.mail import send_mail

if os.path.exists('env.py'):
    import env

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
            user.is_active = False  # Set the associated user to inactive
            user.save()

            profile.is_active = False  # Set the profile to inactive
            profile.save()

            # Send an email to the user
            subject = "Your account has been set as inactive."
            message = "Oh, no! Due to repeated inappropriate comments (5 or more), your account has been set as inactive."
            from_email = os.environ.get('EMAIL_HOST_USER')  
            recipient_list = [user.email]

            send_mail(subject, message, from_email, recipient_list)