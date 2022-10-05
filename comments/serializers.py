from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment

# DRF-API walkthrough used to get guidance on creating comment model
# Original code has been modified to suit project purpose


class CommentSerializer(serializers.ModelSerializer):
    '''
    Comment model serializer
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_on = serializers.SerializerMethodField()
    modified_on = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_on(self, obj):
        return naturaltime(obj.created_on)

    def get_modified_on(self, obj):
        return naturaltime(obj.modified_on)

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'post', 'created_on', 'modified_on', 'content']


class CommentDetailSerializer(CommentSerializer):
    '''
    Serializer for comment model used in Detail View
    '''
    post = serializers.ReadOnlyField(source='post.id')
