# Generated by Django 3.2.19 on 2023-10-28 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_rating_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='user',
            new_name='owner',
        ),
    ]
