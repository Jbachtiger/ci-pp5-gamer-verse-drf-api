from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    '''
    Review model serializer
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        '''
        Return correct user
        '''
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        '''
        Displays fields for views
        '''
        model = Review
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'title', 'content', 'game_publisher', 'game_developer',
            'created_on', 'modified_on', 'game_score', 'genre',
        ]
