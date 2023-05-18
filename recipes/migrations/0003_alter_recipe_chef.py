# Generated by Django 3.2.19 on 2023-05-18 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_recipe_time_effort'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='chef',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
