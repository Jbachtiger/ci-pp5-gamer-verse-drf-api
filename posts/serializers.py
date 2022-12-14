from rest_framework import serializers
from .models import Post
from likes.models import Like

# DRF-API walkthrough used to get guidance on creating post serializer
# Original code has been modified to suit project purpose


class PostSerializer(serializers.ModelSerializer):
    '''
    Post model serializer
    '''
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

# Image validation ensures correct size, height and width of image is uploaded
    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                'Oops! Your image size must be less than 2MB.'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Oops! Your image height must be less than 4096px high.'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Oops! Your image width must be less than 4096 wide.'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'created_on', 'modified_on', 'title', 'description', 'image',
            'game_medium', 'like_id', 'likes_count', 'comments_count',
        ]
