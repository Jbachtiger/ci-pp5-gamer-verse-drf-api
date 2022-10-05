from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    '''
    Events model
    '''
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    city = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    price = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    event_link = models.URLField('Event URL', max_length=500, blank=True)

    class Meta:
        '''
        Order events by date created and display
        most recent first
        '''
    ordering = ['-created_on']

    def __str__(self):
        return f'{self.id} {self.title} {self.date}'
