# Generated by Django 3.2.19 on 2023-06-27 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default='', max_length=50)),
                ('cuisine', models.CharField(choices=[('american', 'AMERICAN'), ('austrian', 'AUSTRIAN'), ('caribbean', 'CARIBBEAN'), ('chinese', 'CHINESE'), ('french', 'FRENCH'), ('german', 'GERMAN'), ('greek', 'GREEK'), ('indian', 'INDIAN'), ('italian', 'ITALIAN'), ('mediterranean', 'Mediterranean'), ('mexican', 'MEXICAN'), ('slovak', 'SLOVAK'), ('spanish', 'SPANISH')], default='american', max_length=13)),
                ('time_effort', models.CharField(default='', max_length=20)),
                ('ingredients', models.TextField(default='')),
                ('description', models.TextField(default='')),
                ('image', models.ImageField(default='../kitchen-ga12e7dca3_1920_ch64p1', upload_to='images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
    ]
