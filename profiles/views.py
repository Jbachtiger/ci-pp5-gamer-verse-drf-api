from rest_framework import generics
from pp5_gamer_verse_drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer

# DRF-API walkthrough used to get guidance on creating profile views


class ProfileList(generics.ListAPIView):
    """
    List all profiles
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    '''
     Retrieve or update profile fields if owner
    '''
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

  

