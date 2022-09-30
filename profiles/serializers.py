from rest_framework import serializers
from .models import Profile

# DRF-API walkthrough used to get guidance on creating profile serializer
# Original code has been modified to suit project purpose
class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_on', 'modified_on', 'name', 
            'favourite_game', 'description', 'image'
        ]