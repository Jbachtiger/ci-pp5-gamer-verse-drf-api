from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# DRF-API walkthrough used to get guidance on creating profile model
# Original code has been modified to suit project purpose


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    favourite_game = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default-profile-240x240_f0iojl'
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.owner}'s profile"

# Everytime a user is created a signal triggers profile model to be created


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
