# Generated by Django 3.2.19 on 2023-05-23 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_chef'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='favorite_cuisine',
        ),
    ]
