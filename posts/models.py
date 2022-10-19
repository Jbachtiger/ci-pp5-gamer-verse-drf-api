from django.db import models
from django.contrib.auth.models import User


# DRF-API walkthrough used to get guidance on creating post model
# Original code has been modified to suit project purpose
class Post(models.Model):
    '''
    Post model related to owner/user
    '''
    game_medium_choices = [
        ('video_games', 'Video games'),
        ('boardgames', 'Boardgames'),
        ('card_games', 'Card games'),
        ('game_art', 'Game art'),
        ('other', 'Other'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    image = models.ImageField(
        upload_to='images/', default='../default-profile-240x240_f0iojl',
        blank=True
    )
    game_medium = models.CharField(
        max_length=15, choices=game_medium_choices, default='games'
    )

    class Meta:
        '''
        Order posts by date and display most recent first
        '''
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'
