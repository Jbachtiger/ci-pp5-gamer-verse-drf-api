from rest_framework import generics, permissions, filters
from pp5_gamer_verse_drf_api.permissions import IsOwnerOrReadOnly
from .models import Event
from .serializers import EventSerializer


class EventList(generics.ListCreateAPIView):
    '''
    Create new events
    '''
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        '''
        Save authenticated events
        '''
        serializer.save(owner=self.request.user)

    filter_backends = [
        filters.SearchFilter,
    ]

    search_fields = [
        'owner__username',
        'title',
        'city',
        'address',
    ]


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve, Update and Destroy events
    '''
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()
