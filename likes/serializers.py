from django.db import IntegrityError
from rest_framework import serializers
from .models import Like

# DRF-API walkthrough used to get guidance on creating comment model
# Original code has been modified to suit project purpose


class LikeSerializer(serializers.ModelSerializer):
    '''
    Like model serializer
    '''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ['id', 'created_on', 'owner', 'post']

    def create(self, validated_data):
        '''
        Creates an error message should a user
        try to like the same post more than once
        '''
        try:
            return super().CREATE(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'duplication'
            })
