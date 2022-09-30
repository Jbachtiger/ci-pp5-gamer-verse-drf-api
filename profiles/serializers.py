from rest_framework import serializers
from .models import Profile

# DRF-API walkthrough used to get guidance on creating profile serializer
# Original code has been modified to suit project purpose
class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner


    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_on', 'modified_on', 'name', 
            'favourite_game', 'description', 'image', 'is_owner'
        ]