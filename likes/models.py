from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

# DRF-API walkthrough used to get guidance on creating comment model
# Original code has been modified to suit project purpose


class Like(models.Model):
    '''
    Like model which is related to 'owner and 'post'
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''
        Post cannot be like more than once by same user
        '''
        ordering = ['-created_on']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'
