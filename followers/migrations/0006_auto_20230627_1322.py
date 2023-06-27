# Generated by Django 3.2.19 on 2023-06-27 13:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('followers', '0005_auto_20230627_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='follower',
            new_name='owner',
        ),
        migrations.AlterUniqueTogether(
            name='follower',
            unique_together={('owner', 'followed')},
        ),
    ]
