from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

CUISINE_CHOICES = (
    ('american','AMERICAN'),
    ('austrian','AUSTRIAN'),
    ('caribbean','CARIBBEAN'),
    ('chinese','CHINESE'),
    ('french', 'FRENCH'),
    ('german', 'GERMAN'),
    ('greek','GREEK'),
    ('indian','INDIAN'),
    ('italian','ITALIAN'),
    ('mediterranean','MEXICAN'),
    ('mexican','MEXICAN'),
    ('slovak', 'SLOVAK'),
    ('spanish','SPANISH'),
)


class Profile(models.Model):
    chef = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_uhncwe'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    favorite_cuisine = models.CharField(max_length=13, choices=CUISINE_CHOICES, default='american')
    bio = models.CharField(max_length=200, default="")

class Meta:
        ordering = ['-updated_at']

def __str__(self):
    return f"{self.chef}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(chef=instance)

post_save.connect(create_profile, sender=User)