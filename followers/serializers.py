from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower

# DRF-API walkthrough used to get guidance on creating follower serializer
# Original code has been modified to suit project purpose


class FollowerSerializer(serializers.ModelSerializer):
    '''
    Followers model serializer
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = [
            'id', 'owner', 'created_on', 'followed', 'followed_name'
        ]

    def create(self, validated_data):
        '''
        Stops user from following another user twice
        '''
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'duplication'})
