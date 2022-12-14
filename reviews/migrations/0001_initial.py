# Generated by Django 3.2.15 on 2022-10-02 13:18

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
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('game_publisher', models.CharField(max_length=255)),
                ('game_developer', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(default='../default-profile-240x240_f0iojl', upload_to='images/')),
                ('game_score', models.CharField(choices=[('1', '1/5'), ('2', '2/5'), ('3', '3/5'), ('4', '4/5'), ('5', '5/5')], default='no score', max_length=10)),
                ('genre', models.CharField(choices=[('sandbox', 'Sandbox'), ('real-time', 'Real-time strategy'), ('shooters', 'Shooters (FPS and TPS)'), ('mmo', 'MMO'), ('role-playing', 'Role-playing'), ('simulation_and_sport', 'Simulation and sports'), ('puzzle_party', 'Puzzler and party'), ('action_adventure', 'Action-adventure'), ('survival_horror', 'Survival and horror'), ('platformer', 'Platformer')], default='other', max_length=50)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
