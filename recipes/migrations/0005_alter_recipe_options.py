# Generated by Django 3.2.19 on 2023-05-22 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-updated_at']},
        ),
    ]