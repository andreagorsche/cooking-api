# Generated by Django 3.2.19 on 2024-03-29 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_rename_user_rating_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='comment',
        ),
    ]
