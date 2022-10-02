from rest_framework import generics, permissions
from pp5_gamer_verse_drf_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer

# DRF-API walkthrough used to get guidance on creating follower serializer
# Original code has been modified to suit project purpose


class FollowerList(generics.ListCreateAPIView):
    '''
    Allows users to follow each other
    '''
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        '''
        Authenticated users follow request saves to database
        '''
        serializer.save(owner=self.request.user)
