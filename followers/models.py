from django.db import models
from django.contrib.auth.models import User

# DRF-API walkthrough used to get guidance on creating follower model
# Original code has been modified to suit project purpose


class Follower(models.Model):
    '''
    Followers model giving users the ability to follow/unfollow other users
    '''
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''
        Stops users from following same profile multiple times
        '''
        ordering = ['created_on']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'
