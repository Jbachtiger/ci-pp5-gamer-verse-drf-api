from rest_framework import generics, permissions, filters
from pp5_gamer_verse_drf_api.permissions import IsOwnerOrReadOnly
from .models import Review
from .serializers import ReviewSerializer


class ReviewList(generics.ListCreateAPIView):
    '''
    Create a new review 
    '''
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()

    def perform_create(self, serializer):
        '''
        Save authenticated reviews 
        '''
        serializer.save(owner=self.request.user)



