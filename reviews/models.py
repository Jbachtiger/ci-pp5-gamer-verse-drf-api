from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    '''
    Reviews model
    '''
    game_score_choices = [
        ('1', '1/5'),
        ('2', '2/5'),
        ('3', '3/5'),
        ('4', '4/5'),
        ('5', '5/5'),
    ]

    genre_choices = [
        ('sandbox', 'Sandbox'),
        ('real_time', 'Real-time strategy'),
        ('shooters', 'Shooters (FPS and TPS)'),
        ('mmo', 'MMO'),
        ('role_playing', 'Role-playing'),
        ('simulation_and_sport', 'Simulation and sports'),
        ('puzzle_party', 'Puzzler and party'),
        ('action_adventure', 'Action and adventure'),
        ('survival_horror', 'Survival and horror'),
        ('platformer', 'Platformer'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    game_publisher = models.CharField(max_length=255)
    game_developer = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', default='../default-profile-240x240_f0iojl'
    )
    game_score = models.CharField(
        max_length=10,
        choices=game_score_choices,
        default='no score'
    )
    genre = models.CharField(
        max_length=50,
        choices=genre_choices,
        default='other'
    )

    class Meta:
        '''
        Order reviews by date created and display
        most recent first
        '''
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title}'
